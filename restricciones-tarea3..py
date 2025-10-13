import numpy as np
import matplotlib.pyplot as plt

def polygon_region(a, b, c, xmin, ymin, xmax, ymax):
    pts = []

    # puntos candidatos: esquinas de la caja
    corners = [(xmin, ymin), (xmin, ymax), (xmax, ymin), (xmax, ymax)]
    for (x, y) in corners:
        if a*x + b*y <= c + 1e-9:  # dentro de la semirrecta
            pts.append((x, y))

    # intersección de la recta con x = xmin
    if b != 0:
        y_at_xmin = (c - a * xmin) / b
        if ymin - 1e-9 <= y_at_xmin <= ymax + 1e-9:
            if a*xmin + b*y_at_xmin <= c + 1e-9:
                pts.append((xmin, y_at_xmin))

    # intersección de la recta con x = xmax
    if b != 0:
        y_at_xmax = (c - a * xmax) / b
        if ymin - 1e-9 <= y_at_xmax <= ymax + 1e-9:
            if a*xmax + b*y_at_xmax <= c + 1e-9:
                pts.append((xmax, y_at_xmax))

    # intersección de la recta con y = ymin
    if a != 0:
        x_at_ymin = (c - b * ymin) / a
        if xmin - 1e-9 <= x_at_ymin <= xmax + 1e-9:
            if a*x_at_ymin + b*ymin <= c + 1e-9:
                pts.append((x_at_ymin, ymin))

    # intersección de la recta con y = ymax
    if a != 0:
        x_at_ymax = (c - b * ymax) / a
        if xmin - 1e-9 <= x_at_ymax <= xmax + 1e-9:
            if a*x_at_ymax + b*ymax <= c + 1e-9:
                pts.append((x_at_ymax, ymax))

    # Filtrar duplicados aproximados
    unique = []
    for p in pts:
        if not any(np.hypot(p[0]-q[0], p[1]-q[1]) < 1e-6 for q in unique):
            unique.append(p)
    pts = unique

    if not pts:
        return []  # región vacía dentro de la caja

    # ordenar puntos en sentido horario (convex hull simple por ángulo respecto al centro)
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    pts.sort(key=lambda p: np.arctan2(p[1]-cy, p[0]-cx))
    return pts

def graficar_restriccion(a, b, c, xmin, ymin, xmax, ymax, titulo, color):
    x = np.linspace(0, xmax, 400)
    # línea (para dibujarla, evitamos división por cero)
    if b != 0:
        y_line = (c - a*x)/b
    else:
        y_line = np.full_like(x, np.nan)

    plt.figure(figsize=(6,5))

    # polígono de la región factible considerando bounds y mínimos
    poly = polygon_region(a, b, c, xmin, ymin, xmax, ymax)
    if poly:
        poly_x, poly_y = zip(*poly)
        plt.fill(poly_x, poly_y, color=color, alpha=0.45, label='Región factible')

    # dibujar la recta (recortada al plotting box)
    if b != 0:
        # limitar la porción visible
        xs = np.linspace(xmin, xmax, 200)
        ys = (c - a*xs)/b
        # solo dibujar donde ys está dentro del plot
        valid = (ys >= ymin - 1e-6) & (ys <= ymax + 1e-6)
        if valid.any():
            plt.plot(xs[valid], ys[valid], 'r-', linewidth=2, label=f'{a}x + {b}y = {c}')
    else:
        # recta vertical a*x = c  => x = c/a
        if a != 0:
            xv = c / a
            if xmin-1e-9 <= xv <= xmax+1e-9:
                plt.plot([xv, xv], [ymin, ymax], 'r-', linewidth=2, label=f'{a}x + {b}y = {c}')

    # dibujar líneas de mínimos si aplican
    if xmin > 0:
        plt.axvline(xmin, color='orange', linewidth=2, label=f'x = {xmin}')
    if ymin > 0:
        plt.axhline(ymin, color='blue', linewidth=2, label=f'y = {ymin}')

    # ejes y limites
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(titulo)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Ejercicio 1: x ≥ 5, x + y ≤ 15
graficar_restriccion(a=1, b=1, c=15, xmin=5, ymin=0, xmax=16, ymax=16,
                     titulo="Ejercicio 1: x ≥ 5, x + y ≤ 15", color='lightblue')

# Ejercicio 2: 3x + 5y ≤ 20 (sin mínimos extra)
graficar_restriccion(a=3, b=5, c=20, xmin=0, ymin=0, xmax=8, ymax=6,
                     titulo="Ejercicio 2: 3x + 5y ≤ 20", color='lightgreen')

# Ejercicio 3: x ≥ 4, y ≥ 6, x + y ≤ 12
graficar_restriccion(a=1, b=1, c=12, xmin=4, ymin=6, xmax=13, ymax=13,
                     titulo="Ejercicio 3: x ≥ 4, y ≥ 6, x + y ≤ 12", color='lightcoral')

# Ejercicio 4: 2x + 3y ≤ 18
graficar_restriccion(a=2, b=3, c=18, xmin=0, ymin=0, xmax=10, ymax=8,
                     titulo="Ejercicio 4: 2x + 3y ≤ 18", color='khaki')

# Ejercicio 5: 5x + 10y ≤ 50 (ó x + 2y ≤ 10)
graficar_restriccion(a=5, b=10, c=50, xmin=0, ymin=0, xmax=11, ymax=6,
                     titulo="Ejercicio 5: 5x + 10y ≤ 50", color='plum')
