import matplotlib.pyplot as plt

# Define the functions
f = lambda x: -(x**4)/2 + 4*x**3 - 10*x**2 + 8.5*x + 1
dy = lambda x: -(2*x**3) + 12*x*x - 20*x + 8.5

# Initial values
x = 0
xn = 4
y = 1
h = 0.5
n = int((xn - x) / h)

# Lists to store values for plotting
x_values = [x]
y_euler_values = [y]
y_analytical_values = [f(x)]

# Euler's method loop
for i in range(n):
    y += dy(x) * h
    x += h
    x_values.append(x)
    y_euler_values.append(y)
    y_analytical_values.append(f(x))

# Print table
print('x \t\ty(Euler) \ty(Analytical)')
for i in range(len(x_values)):
    print('%f \t%f \t%f' % (x_values[i], y_euler_values[i], y_analytical_values[i]))

# Plot the results
plt.plot(x_values, y_euler_values, label='Euler Method')
plt.plot(x_values, y_analytical_values, label='Analytical Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
