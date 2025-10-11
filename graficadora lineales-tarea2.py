def obtener_valores(funcion):
    f = funcion.replace(" ", "").lower()
    if f.startswith("y="): f = f[2:]
    if "x" not in f:
        return 0, float(f)
    i = f.index("x")
    m = f[:i]
    m = 1 if m in ["", "+"] else -1 if m == "-" else float(m)
    b = float(f[i+1:]) if f[i+1:] else 0
    return m, b

def graficar(m1, b1, m2, b2):
    interx = (b2 - b1) / (m1 - m2) if m1 != m2 else None
    intery = m1 * interx + b1 if interx is not None else None

    for y in range(20, -21, -1):
        linea = ""
        for x in range(-20, 21):
            y1, y2 = round(m1*x + b1), round(m2*x + b2)
            if y == round(intery) and x == round(interx):
                linea += "#"
            elif y == y1:
                linea += "*"
            elif y == y2:
                linea += "o"
            elif x == 0 and y == 0:
                linea += "+"
            elif x == 0:
                linea += "|"
            elif y == 0:
                linea += "-"
            else:
                linea += " "
        print(linea)

    print("\nLeyenda del gráfico:")
    print("* = Función 1 (Function 1)")
    print("o = Función 2 (Function 2)")
    print("# = Intersección (Intersection)")
    print("| = Eje Y (Y-axis)")
    print("- = Eje X (X-axis)")
    print("+ = Origen (0,0) (Origin (0,0))")

    if interx is not None:
        print(f"\nPunto de intersección: ({interx:.2f}, {intery:.2f})")
    else:
        print("\nLas rectas son paralelas (no se intersectan).")

print("=== GRAFICADOR DE FUNCIONES LINEALES ===")
f1 = input("Función 1 (ej: 2x+3): ")
f2 = input("Función 2 (ej: -x-4): ")

m1, b1 = obtener_valores(f1)
m2, b2 = obtener_valores(f2)

graficar(m1, b1, m2, b2)

