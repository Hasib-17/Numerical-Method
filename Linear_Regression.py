import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Take input for x and y
n = int(input("Enter the number of data points: "))
x_values = np.array([float(input(f"Enter x[{i+1}]: ")) for i in range(n)]).reshape(-1, 1)
y_values = np.array([float(input(f"Enter y[{i+1}]: ")) for i in range(n)]).reshape(-1, 1)

model = LinearRegression()
model.fit(x_values, y_values)

    # Extract coefficients
a0 = model.intercept_[0]
a1 = model.coef_[0][0]

    # Print the coefficients for linear regression
print(f'Intercept (a0): {a0:.4f}')
print(f'Slope     (a1): {a1:.4f}')

    # Plot the data points
plt.scatter(x_values, y_values, color='blue', label='Data points')

    # Plot the linear regression line
regression_line = a0 + a1 * x_values
plt.plot(x_values, regression_line, color='red', label=f'Linear Regression: y = {a0:.4f} + {a1:.4f}x')

    # Add labels and legend
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

    # Show the plot
plt.show()


