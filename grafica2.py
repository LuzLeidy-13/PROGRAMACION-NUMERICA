import numpy as np
import matplotlib.pyplot as plt

def ejercicio2():
    x = np.linspace(0, 8, 200)
    y = (20 - 3*x) / 5  # Línea de restricción: 3x + 5y = 20

    plt.figure(figsize=(7,6))

    # Región factible: 3x + 5y ≤ 20, x ≥ 0, y ≥ 0
    x_fill = np.linspace(0, 8, 200)
    y_fill = np.maximum(0, (20 - 3*x_fill)/5)
    plt.fill_between(x_fill, 0, y_fill, color='lightgreen', alpha=0.5)

    plt.plot(x, y, 'r-', linewidth=2, label='3x + 5y = 20')

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.xlim(0, 8)
    plt.ylim(0, 6)
    plt.xlabel("x (horas servidor A)")
    plt.ylabel("y (horas servidor B)")
    plt.title("Restricción: 3x + 5y ≤ 20, x,y ≥ 0")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()
    
ejercicio2()


