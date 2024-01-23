import matplotlib.pyplot as plt
from tabulate import tabulate
from math import e

def secant(f, x1, x2,trueRoot, tolerance=1e-6, maxiter=100):
    iteration_data = []

    for iterations in range(1, maxiter + 1):
        # Calculate the new approximation using the secant equation
        # 
        xnew = x2 - (x2 - x1) / (f(x2) - f(x1)) * f(x2)
        
        TrueError = (abs(trueRoot-xnew)/trueRoot)*100


        # Store iteration data for later display
        iteration_data.append([iterations, x1, x2, xnew, TrueError])

        # Check for convergence
        if abs(xnew - x2) < tolerance:
            break

        # Update values for the next iteration
        x1 = x2
        x2 = xnew

    else:
        # Raise an OverflowError if the maximum number of iterations is reached
        raise OverflowError("Maximum number of iterations reached!")

    return xnew, iterations, iteration_data

# Get user input for the function and initial interval
# f = lambda x: 2 * x**2 - 5 * x + 3
f = lambda x: e**-x - x

# Get user input for the initial interval
x1, x2 = map(float, input("Enter the initial interval (x1 x2): ").split())
trueRoot = float(input("Enter the true root: "))

try:
    # Find the root using the secant method
    xnew, iterations, iteration_data = secant(f, x1, x2,trueRoot)
except OverflowError as e:
    # Handle the OverflowError and exit the program
    print(e)
    exit()

# Display the results for each iteration
iteration_header = ["Iteration", "x1", "x2", "xnew", "Et(True error)"]
print(tabulate(iteration_data, headers=iteration_header, tablefmt="pretty"))

# Display the final result
print('\nThe Root: %0.5f' % xnew)
print('The Number of Iterations: %d' % iterations)

# Plotting the iteration process
x_values = [data[2] for data in iteration_data] + [xnew]
y_values = [data[4] for data in iteration_data] + [f(xnew)]

plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Secant Method Iteration Process')
plt.grid(True)
plt.show()
