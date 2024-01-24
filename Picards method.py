import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
def f(x, y):
    return 1 + x * y
def picards_method_integral(x0, y0, h, num_iterations):
    x_values = [x0]
    y_values = [y0]

    for _ in range(num_iterations):
        x = x_values[-1]  # -1 MEANS X0,Y0
        y_integral = integrate.quad(lambda x: f(x, y_values[-1]), x_values[-1], x_values[-1] + h)[0]
        y = y_values[-1] + y_integral # Y0+INTRGRAL PART SUTRO
        x_values.append(x + h)
        y_values.append(y)

        print(f"At x = {x + h:.2f}, y = {y:.3f}")

    return x_values, y_values

# Initial conditions
x0 = 0
y0 = 1
h = 0.1
num_iterations = 5

# Apply Picard's method with integral
x_values_integral, y_values_integral = picards_method_integral(x0, y0, h, num_iterations)

plt.scatter(x_values_integral, y_values_integral, color='red', label='Picard\'s Method Points (Integral)')

# Connect the points with lines
plt.plot(x_values_integral, y_values_integral, linestyle='--', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Picard's Method with Integral Curve")
plt.legend()
plt.grid(True)
plt.show()
