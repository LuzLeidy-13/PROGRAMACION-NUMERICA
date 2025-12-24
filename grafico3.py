import numpy as np
import matplotlib.pyplot as plt

def ejercicio3():
 
    x = np.linspace(0, 13, 200)
    y_linea = 12 - x  # Línea de restricción x + y = 12

    plt.figure(figsize=(7,6))

    x_fill = np.linspace(4, 6, 200)  
    y_fill = 12 - x_fill
    plt.fill_between(x_fill, 6, y_fill, color='lightcoral', alpha=0.5)

    plt.axvline(4, color='orange', linewidth=2, label='x = 4')
    plt.axhline(6, color='blue', linewidth=2, label='y = 6')
    plt.plot(x, y_linea, 'r-', linewidth=2, label='x + y = 12')

    # Ejes
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # Configuración del gráfico
    plt.xlim(0, 13)
    plt.ylim(0, 13)
    plt.xlabel("x (horas de reuniones)")
    plt.ylabel("y (horas de documentación)")
    plt.title("Restricciones: x ≥ 4, y ≥ 6, x + y ≤ 12")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()

ejercicio3()
