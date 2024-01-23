import numpy as np
import matplotlib.pyplot as plt
def milnes_predictor(x, y):
    h = 0.5

    y_pred = y[0] + 4*(h / 3) * (
        2 * 0.5 * (x[1] + y[1]) -
        1 * 0.5 * (x[2] + y[2]) +
        2 * 0.5 * (x[3] + y[3])
    )

    print(f"At x = {x[4]}, y_predict_value = {y_pred:.5f}")

    y_corr = y[2] + (h / 3) * (
        1 * 0.5 * (x[2] + y[2]) +
        4 * 0.5 * (x[3] + y[3]) +
        1 * 0.5 * (x[4] + y_pred)
    )
    print(f"At x = {x[4]}, y_correct_value = {y_corr:.5f}")

    # Plot the curve only for the corrector point
    plt.plot(x[4], y_corr, label="Milne's Predictor-Corrector Curve (Corrector Point)", marker='o', color='blue')

    # Connect the points from 0 to 0.5 to 1 to 1.5 and finally to the corrector point
    plt.plot([x[0], x[1], x[2], x[3], x[4]], [y[0], y[1], y[2], y[3], y_corr], linestyle='--', color='blue', marker='o')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title("Milne's Predictor-Corrector Method")
    plt.show()

x = np.array([0, 0.5, 1, 1.5, 2])
y = np.array([2, 2.636, 3.595, 4.968, 0])  # Placeholder for y4

milnes_predictor(x, y)  # function call
