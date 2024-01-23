import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

f = lambda x: 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5
a = 0
b = 0.8
h = (b - a)

x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)

# Simpson's 1/3 rule
I_approx = h * 0.5 * (f(a) + f(b))
print("Approximated Integral using Trapezoid Rule, I_approx_simpson = %f" % I_approx)

# Calculate the true integral using scipy
I_true, _ = integrate.quad(f, a, b)
print("True Integral, I_true = %f" % I_true)

# Calculate absolute error
error_simpson = ((I_true - I_approx) / I_true) * 100
print("Relative Error using Trapezoid Rule = %f%%" % error_simpson)

# Plotting the graph
fig, ax = plt.subplots()

# Plotting the error area in red
ax.fill_between(x_vals, f(x_vals), alpha=0.4, color='red', label='Error Area')

# Plotting the Simpson's 1/3 rule area in orange
ax.fill_between([a, b], [f(a), f(b)], alpha=0.6, color='green', label="Trapezoid Rule Area")

ax.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trapezoidal Rule for Numerical Integration with Error Visualization')
plt.show()
