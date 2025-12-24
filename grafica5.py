import numpy as np
import matplotlib.pyplot as plt

def ejercicio5():
  
    # Rango de valores
    x = np.linspace(0, 11, 200)
    y = (50 - 5*x) / 10  # Línea de restricción

    # Crear figura
    plt.figure(figsize=(7,6))

    # Región factible: debajo de la línea y ≥ 0
    x_fill = np.linspace(0, 10, 200)
    y_fill = np.maximum(0, (50 - 5*x_fill) / 10)
    plt.fill_between(x_fill, 0, y_fill, color='lightblue', alpha=0.5)

    # Dibujar la línea de restricción
    plt.plot(x, y, 'r-', linewidth=2, label='5x + 10y = 50')

    # Ejes
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # Configuración del gráfico
    plt.xlim(0, 11)
    plt.ylim(0, 6)
    plt.xlabel("x (dispositivos tipo A)")
    plt.ylabel("y (dispositivos tipo B)")
    plt.title("Restricción: 5x + 10y ≤ 50, x,y ≥ 0")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    # Mostrar
    plt.show()

# Ejecutar
ejercicio5()
