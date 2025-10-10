# -- coding: utf-8 --
# Graficar restricciones lineales y sombrear región factible (ASCII)

def graficar_ascii(restricciones, xmin=-10, xmax=10, ymin=-10, ymax=10):
    ancho = xmax - xmin + 1
    alto = ymax - ymin + 1

    # Creamos una matriz vacía (plano cartesiano)
    plano = [[" " for _ in range(ancho)] for _ in range(alto)]

    # Dibujar ejes
    for y in range(alto):
        for x in range(ancho):
            if x + xmin == 0 and y == alto // 2:
                plano[y][x] = "+"
            elif x + xmin == 0:
                plano[y][x] = "|"
            elif y == alto // 2:
                plano[y][x] = "-"

    # Dibujar restricciones
    simbolos = ["*", "o", "#", "x", "+", "%"]
    for i, (a, b, c, signo) in enumerate(restricciones):
        simbolo = simbolos[i % len(simbolos)]

        for x in range(xmin, xmax + 1):
            try:
                if b != 0:
                    y = (c - a * x) / b  # despeje: ax + by = c
                    if isinstance(y, (int, float)):
                        xi = x - xmin
                        yi = alto // 2 - int(round(y))
                        if 0 <= yi < alto and 0 <= xi < ancho:
                            plano[yi][xi] = simbolo
                else:
                    # Recta vertical: ax = c
                    if a != 0 and abs(x - c / a) < 0.5:
                        for y in range(alto):
                            plano[y][x - xmin] = simbolo
            except:
                pass

        # Sombrear región factible
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                try:
                    xi = x - xmin
                    yi = alto // 2 - y
                    if 0 <= yi < alto and 0 <= xi < ancho:
                        expr = a * x + b * y
                        if (signo == "<=" and expr <= c) or (signo == ">=" and expr >= c):
                            if plano[yi][xi] == " ":
                                plano[yi][xi] = "."
                except:
                    pass

    # Imprimir plano
    for fila in plano:
        print("".join(fila))

    # Leyenda
    print("\nLeyenda del gráfico:")
    for i, (a, b, c, signo) in enumerate(restricciones):
        print(f"{simbolos[i % len(simbolos)]} = recta {a}x + {b}y = {c}, región {signo}")
    print("| = Eje Y")
    print("- = Eje X")
    print("+ = Origen (0,0)")
    print(". = Región factible")


def main():
    print("\n--- Graficador de Restricciones Lineales ---")
    n = int(input("¿Cuántas restricciones deseas graficar? "))

    restricciones = []
    for i in range(n):
        print(f"\nRestricción {i+1}: forma general ax + by <=/>= c")
        a = float(input("Ingrese a: "))
        b = float(input("Ingrese b: "))
        c = float(input("Ingrese c: "))
        signo = input("Ingrese el signo (<= o >=): ").strip()

        restricciones.append((a, b, c, signo))

    xmin = int(input("\nIngrese xmin: "))
    xmax = int(input("Ingrese xmax: "))
    ymin = int(input("Ingrese ymin: "))
    ymax = int(input("Ingrese ymax: "))

    graficar_ascii(restricciones, xmin, xmax, ymin, ymax)


main()
