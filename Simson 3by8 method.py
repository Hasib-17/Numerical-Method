import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = 0
b = 0.8
c = (b - a) / 3
d = (b - a) / 3 * 2

x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)

# Simpson's 3/8 rule
I_approx = (b - a) * (1/8) * (f(a) + 3*f(c) + 3*f(d) + f(b))
print("Approximated Integral using Simpson's 3/8 Rule, I_approx_simpson = %f" % I_approx)

# Calculate the true integral using scipy
I_true, _ = integrate.quad(f, a, b)
print("True Integral, I_true = %f" % I_true)

# Calculate absolute error
error_simpson = ((I_true - I_approx) / I_true) * 100
print("Relative Error using Simpson's 3/8 Rule = %f%%" % error_simpson)

# Plotting the graph
fig, ax = plt.subplots()

# Plotting the error area in red
ax.fill_between(x_vals, f(x_vals), alpha=1, color='red', label='Error Area')

# Plotting the Simpson's 3/8 rule area with a cubic polynomial curve in green
poly_coefficients = np.polyfit([a, c, d, b], [f(a), f(c), f(d), f(b)], 3)
poly = np.poly1d(poly_coefficients)
x_poly = np.linspace(a, b, 200)
y_poly = poly(x_poly)

ax.fill_between(x_poly, y_poly, alpha=1, color='green', label="Simpson's 3/8 Rule Area")

ax.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simpson\'s 3/8 Rule for Numerical Integration with Error Visualization')
plt.show()
