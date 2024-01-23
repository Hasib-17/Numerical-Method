# Import necessary libraries
from math import sqrt
from tabulate import tabulate
import matplotlib.pyplot as plt

# Get user input for initial value and precision
x = float(input("Enter the initial value: "))
precision = float(input("Enter the precision (e.g., 1e-6): "))

# Initialize variables for convergence check
diff1 = 1e9     # Initial |xnew - x| is taken any higher value e.g., 1×10^9
divergence = 0  # diff in each iteration has to decrease to achieve convergence
iterations = 0

# Lists to store values for plotting and iteration details
x_values = [x]
y_values = [x]
iteration_data = []

# Start the iterative process
while True:
    # Update xnew based on the given formula
    xnew = 0.5 * pow(x, 2) + 0.25

    # Calculate the absolute difference between x and xnew
    diff2 = abs(x - xnew)

    # Check for divergence
    if diff2 > diff1:
        divergence = 1
        break

    # Update diff1 for the next iteration
    diff1 = diff2

    # Increment the iteration count
    iterations += 1

    # Store iteration details for tabulation
    iteration_data.append([iterations, x, xnew])

    # Check if the absolute difference is less than the specified precision
    if abs(xnew - x) < precision:
        break

    # Update x for the next iteration
    x = xnew

    # Store values for plotting
    x_values.append(x)
    y_values.append(xnew)

# Display the results
if divergence == 0:
    # this table optional, it initially show direect final result with total iteration
    result_list = [["Root", xnew], ["Iterations", iterations]]
    header = ["Property", "Value"]
    print(tabulate(result_list, headers=header, tablefmt="pretty"))

    # Display the step-by-step iteration table
    iteration_header = ["Iteration", "x", "xnew"]
    print(tabulate(iteration_data, headers=iteration_header, tablefmt="pretty"))

    # Plotting the iteration process
    plt.plot(x_values, label='x')
    plt.plot(y_values, label='xnew')
    plt.xlabel('Iterations')
    plt.ylabel('Values')
    plt.legend()
    plt.show()
else:
    print("Divergence Case")
