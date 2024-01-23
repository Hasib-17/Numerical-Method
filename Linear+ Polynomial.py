import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Take input for x and y
n = int(input("Enter the number of data points: "))
x_values = np.array([float(input(f"Enter x[{i+1}]: ")) for i in range(n)]).reshape(-1, 1)
y_values = np.array([float(input(f"Enter y[{i+1}]: ")) for i in range(n)]).reshape(-1, 1)

# Take input for polynomial degree
degree = int(input("Enter the degree of the polynomial: "))

if degree == 1:
    # Perform linear regression
    model = LinearRegression()
    model.fit(x_values, y_values)

    # Extract coefficients
    a0 = model.intercept_[0]
    a1 = model.coef_[0][0]

    # Print the coefficients for linear regression
    print(f'Intercept (a0): {a0:.4f}')
    print(f'Slope (a1): {a1:.4f}')

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

else:
    # Transform the input features to include polynomial terms up to the specified degree
    poly_features = PolynomialFeatures(degree=degree)
    x_poly = poly_features.fit_transform(x_values)

    # Perform polynomial regression
    poly_model = LinearRegression()
    poly_model.fit(x_poly, y_values)

    # Print the coefficients for polynomial regression
    print('Polynomial Regression Coefficients:')
    for i in range(degree + 1):
        print(f'a{i}: {poly_model.coef_[0][i]:.4f}')

    # Plot the data points
    plt.scatter(x_values, y_values, color='blue', label='Data points')

    # Plot the polynomial regression curve
    x_range = np.linspace(min(x_values), max(x_values), 100).reshape(-1, 1)
    x_range_poly = poly_features.transform(x_range)
    y_pred = poly_model.predict(x_range_poly)
    plt.plot(x_range, y_pred, color='red', label=f'Polynomial Regression (Degree {degree})')

    # Add labels and legend
    plt.title('Polynomial Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # Show the plot
    plt.show()
