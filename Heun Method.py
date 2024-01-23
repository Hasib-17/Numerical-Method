import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

h = 0.1
x = np.array([0, 0.1, 0.2])
y = np.array([0])

y0p = y[0] + h * (x[0] + 2 * y[0])
y0c = y[0] + h * ((x[0] + 2 * y[0]) + (0.1 + 2 * y0p)) / 2
y1p = y0c + h * (0.1 + 2 * y0c)
y1c = y0c + h * ((0.1 + 2 * y0p) + (0.2 + 2 * y1p)) / 2

# Create a table
table = [["x", "y_predict_value", "y_correct_value"],
         [x[0], y0p, y0c],
         [x[1], y1p, y1c]]

# Print the table
print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

# Plot the graph
plt.plot([x[0], x[1]], [y[0], y0c], label='Milne\'s Predictor-Corrector Curve', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Milne's Predictor-Corrector Method")
plt.show()
