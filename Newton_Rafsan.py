from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff

def func(x):
    return x**2 - 3

def derivative(x):
    # Calculate the derivative of the function
    x_symbol = symbols('x')
    f_prime = diff(func(x_symbol), x_symbol)
    return f_prime.evalf(subs={x_symbol: x})

def newton_raphson(initial_guess, num_iterations):
    x_current = initial_guess
    result_list = []

    for iteration in range(1, num_iterations + 1):
        f_x_current = func(x_current)
        f_prime_x_current = derivative(x_current)

        # Newton-Raphson formula
        x_next = x_current - (f_x_current / f_prime_x_current)

        result_list.append([x_current, f_x_current, f_prime_x_current, x_next])

        if f_x_current == 0:
            return x_current
        x_current = x_next

    header = ["x_current", "f(x_current)", "f'(x_current)", "x_next"]
    print(tabulate(result_list, headers=header, tablefmt="pretty"))

    # Plotting the function
    x_values = np.linspace(initial_guess - 1, initial_guess + 1, 100)
    y_values = func(x_values)
    
    plt.plot(x_values, y_values, label='f(x) = x^2 - 3')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.axvline(x_current, color='red', linestyle='--', label='Root (x_current)')
    
    plt.scatter(x_current, func(x_current), color='red')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Newton-Raphson Method')
    plt.legend()
    plt.grid(True)
    plt.show()

    return x_current

initial_guess = float(input("Enter the initial guess: "))
num_iterations = int(input("Enter the number of iterations: "))
newton_raphson(initial_guess, num_iterations)
