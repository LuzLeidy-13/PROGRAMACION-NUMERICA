import math
import re
import matplotlib.pyplot as plt

# ============================================
# FUNCIÓN BASE: PROCESAMIENTO DE ENTRADA
# ============================================

def preparar_funcion(expr):
    expr = expr.lower().strip()
    expr = expr.replace("^", "**")
    expr = expr.replace("sen", "sin")
    expr = expr.replace("ln", "log")
    expr = expr.replace("π", "pi")
    # Multiplicaciones implícitas: 2x → 2*x, xsin(x) → x*sin(x)
    expr = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z\)])(\d)', r'\1*\2', expr)
    return expr

def f_factory(funcion_str):
    def f(x):
        try:
            return eval(funcion_str, {"__builtins__": None}, math.__dict__ | {"x": x})
        except Exception:
            return None
    return f

def graficar(f, xr, titulo):
    xs = [xr + i * 0.1 for i in range(-50, 51)]
    ys = [f(x) for x in xs]
    plt.figure()
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.plot(xs, ys, label="f(x)", color="blue")
    plt.scatter([xr], [f(xr)], color="red", label=f"Raíz ≈ {xr:.5f}")
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.show()

# ============================================
# MÉTODO DE BISECCIÓN
# ============================================

def biseccion():
    print("\n=== MÉTODO DE BISECCIÓN ===")
    funcion_str = preparar_funcion(input("Ingrese la función f(x): "))
    f = f_factory(funcion_str)
    x1 = float(input("Ingrese x1 = "))
    x2 = float(input("Ingrese x2 = "))

    tol = 1e-10
    max_iter = 100
    itera = 0
    xr = x1
    error = 1

    print(f"{'Itera':<6} {'xr':<15} {'error':<15} {'f(xr)':<15}")
    print("-" * 55)

    while itera < max_iter and error > tol:
        xant = xr
        xr = (x1 + x2) / 2
        fx1, fxr = f(x1), f(xr)
        if fx1 * fxr < 0:
            x2 = xr
        else:
            x1 = xr
        error = abs(xr - xant)
        itera += 1
        print(f"{itera:<6} {xr:<15.10f} {error:<15.10f} {f(xr):<15.10f}")

    print(f"\nRaíz aproximada: {xr:.10f}")
    graficar(f, xr, "Método de Bisección")

# ============================================
# MÉTODO DE REGULA FALSI
# ============================================

def regula_falsi():
    print("\n=== MÉTODO DE REGULA FALSI ===")
    funcion_str = preparar_funcion(input("Ingrese la función f(x): "))
    f = f_factory(funcion_str)
    x1 = float(input("Ingrese x1 = "))
    x2 = float(input("Ingrese x2 = "))

    tol = 1e-10
    max_iter = 100
    itera = 0
    xr = x1
    error = 1

    print(f"{'Itera':<6} {'xr':<15} {'error':<15} {'f(xr)':<15}")
    print("-" * 55)

    while itera < max_iter and error > tol:
        xant = xr
        fx1, fx2 = f(x1), f(x2)
        xr = x2 - fx2 * (x2 - x1) / (fx2 - fx1)
        fxr = f(xr)
        if fx1 * fxr < 0:
            x2 = xr
        else:
            x1 = xr
        error = abs(xr - xant)
        itera += 1
        print(f"{itera:<6} {xr:<15.10f} {error:<15.10f} {fxr:<15.10f}")

    print(f"\nRaíz aproximada: {xr:.10f}")
    graficar(f, xr, "Método de Regula Falsi")

# ============================================
# MÉTODO DE SECANTE
# ============================================

def secante():
    print("\n=== MÉTODO DE SECANTE ===")
    funcion_str = preparar_funcion(input("Ingrese la función f(x): "))
    f = f_factory(funcion_str)
    x1 = float(input("Ingrese x1 = "))
    x2 = float(input("Ingrese x2 = "))

    tol = 1e-10
    max_iter = 100
    itera = 0
    xr = x1
    error = 1

    print(f"{'Itera':<6} {'xr':<15} {'error':<15} {'f(xr)':<15}")
    print("-" * 55)

    while itera < max_iter and error > tol:
        xant = xr
        fx1, fx2 = f(x1), f(x2)
        xr = x2 - fx2 * (x2 - x1) / (fx2 - fx1)
        x1, x2 = x2, xr
        error = abs(xr - xant)
        itera += 1
        print(f"{itera:<6} {xr:<15.10f} {error:<15.10f} {f(xr):<15.10f}")

    print(f"\nRaíz aproximada: {xr:.10f}")
    graficar(f, xr, "Método de la Secante")

# ============================================
# MÉTODO DE PUNTO FIJO
# ============================================

def punto_fijo():
    print("\n=== MÉTODO DE PUNTO FIJO ===")
    g_str = preparar_funcion(input("Ingrese la función g(x): "))
    g = f_factory(g_str)
    x0 = float(input("Ingrese x0 = "))

    tol = 1e-10
    max_iter = 100
    itera = 0
    xr = x0
    error = 1

    print(f"{'Itera':<6} {'xr':<15} {'error':<15}")
    print("-" * 40)

    while itera < max_iter and error > tol:
        xant = xr
        xr = g(xant)
        if xr is None:
            break
        error = abs(xr - xant)
        itera += 1
        print(f"{itera:<6} {xr:<15.10f} {error:<15.10f}")

    print(f"\nRaíz aproximada: {xr:.10f}")
    graficar(lambda x: g(x) - x, xr, "Método de Punto Fijo")

# ============================================
# MÉTODO DE NEWTON-RAPHSON
# ============================================

def newton_raphson():
    print("\n=== MÉTODO DE NEWTON-RAPHSON ===")
    funcion_str = preparar_funcion(input("Ingrese la función f(x): "))
    f = f_factory(funcion_str)
    x0 = float(input("Ingrese x0 = "))
    h = 1e-6

    def fprima(x):  # derivada numérica
        return (f(x + h) - f(x - h)) / (2 * h)

    tol = 1e-10
    max_iter = 100
    itera = 0
    xr = x0
    error = 1

    print(f"{'Itera':<6} {'xr':<15} {'error':<15} {'f(xr)':<15}")
    print("-" * 55)

    while itera < max_iter and error > tol:
        xant = xr
        d = fprima(xr)
        if d == 0 or d is None:
            print("Derivada nula. Método detenido.")
            break
        xr = xr - f(xr) / d
        error = abs(xr - xant)
        itera += 1
        print(f"{itera:<6} {xr:<15.10f} {error:<15.10f} {f(xr):<15.10f}")

    print(f"\nRaíz aproximada: {xr:.10f}")
    graficar(f, xr, "Método de Newton-Raphson")

# ============================================
# MENÚ PRINCIPAL
# ============================================

while True:
    print("\n=== MÉTODOS NUMÉRICOS ===")
    print("1. Bisección")
    print("2. Regula Falsi")
    print("3. Secante")
    print("4. Punto Fijo")
    print("5. Newton-Raphson")
    print("0. Salir")

    op = input("Seleccione un método: ")

    if op == "1":
        biseccion()
    elif op == "2":
        regula_falsi()
    elif op == "3":
        secante()
    elif op == "4":
        punto_fijo()
    elif op == "5":
        newton_raphson()
    elif op == "0":
        break
    else:
        print("Opción inválida.")
