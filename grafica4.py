import numpy as np
import matplotlib.pyplot as plt

def ejercicio4():
  
    # Rango de valores
    x = np.linspace(0, 10, 200)
    y = (18 - 2*x) / 3  # Línea de restricción

    # Crear figura
    plt.figure(figsize=(7,6))

    # Región factible: debajo de la línea y ≥ 0
    x_fill = np.linspace(0, 9, 200)
    y_fill = np.maximum(0, (18 - 2*x_fill) / 3)
    plt.fill_between(x_fill, 0, y_fill, color='lightgreen', alpha=0.5)

    # Dibujar la línea de restricción
    plt.plot(x, y, 'r-', linewidth=2, label='2x + 3y = 18')

    # Ejes
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # Configuración del gráfico
    plt.xlim(0, 10)
    plt.ylim(0, 8)
    plt.xlabel("x (tiempo en assets 2D)")
    plt.ylabel("y (tiempo en assets 3D)")
    plt.title("Restricción: 2x + 3y ≤ 18, x,y ≥ 0")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    # Mostrar
    plt.show()

# Ejecutar
ejercicio4()
