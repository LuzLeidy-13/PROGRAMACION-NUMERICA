import numpy as np
import matplotlib.pyplot as plt

def ejercicio1():
    # Rango de valores
    x = np.linspace(0, 16, 200)
    y = 15 - x  # Línea: x + y = 15

    # Crear figura
    plt.figure(figsize=(7,6))

    # Dibujar región factible: x ≥ 5, y ≥ 0, x + y ≤ 15
    x_fill = np.linspace(5, 15, 200)
    y_fill = 15 - x_fill
    plt.fill_between(x_fill, 0, y_fill, color='lightblue', alpha=0.5)

    # Dibujar líneas de restricción
    plt.plot(x, y, 'r-', label='x + y = 15')
    plt.axvline(5, color='orange', label='x = 5')

    # Ejes
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # Configuración del gráfico
    plt.xlim(0, 16)
    plt.ylim(0, 16)
    plt.xlabel("x (front-end)")
    plt.ylabel("y (back-end)")
    plt.title("Restricciones: x ≥ 5, x + y ≤ 15, x,y ≥ 0")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    # Mostrar
    plt.show()

# Ejecutar
ejercicio1()



