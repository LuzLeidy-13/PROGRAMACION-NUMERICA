import math, re, matplotlib.pyplot as plt

print("=== MÉTODO DEL PUNTO FIJO ===")

def preparar_funcion(expr):
    expr = expr.lower().strip()
    expr = expr.replace("^", "**").replace("sen", "sin").replace("ln", "log").replace("π", "pi")
    expr = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z\)])(\d)', r'\1*\2', expr)
    return expr

# --- Ingreso de la función original ---
funcion_f = input("Ingrese la función f(x): (ejemplo: e^x - 4x) → ")
funcion_f = preparar_funcion(funcion_f)

g_str = None

match = re.match(r"e\*\*x\s*-\s*(\d+)\*?x", funcion_f)
if match:
    a = float(match.group(1))
    g_str = f"log({a}*x)"
    print(f"Transformación detectada automáticamente:  g(x) = ln({a}x)")

# Si no se reconoce, pedir g(x)
if g_str is None:
    print("No se detectó una transformación automática.")
    g_str = input("Ingrese la transformación g(x): ")

# --- Definir funciones ---
def f(x):
    try:
        return eval(funcion_f, {"__builtins__": None}, math.__dict__ | {"x": x})
    except:
        return None

def g(x):
    try:
        return eval(preparar_funcion(g_str), {"__builtins__": None}, math.__dict__ | {"x": x})
    except:
        return None

# --- Parámetros iniciales ---
x0 = float(input("Ingrese el valor inicial x0 = "))
tol = 1e-10
max_iter = 100

itera = 0
xr = x0
error = 100
valores = [x0]

print(f"\n{'Itera':<6} {'x_i':<15} {'x_i+1':<15} {'f(x)':<15} {'g(x)':<15} {'Error(%)':<10}")
print("-" * 80)

# --- Iteraciones ---
while itera < max_iter and error > tol:
    x_ant = xr
    xr = g(x_ant)
    if xr is None:
        break
    fx = f(x_ant)
    error = abs((xr - x_ant) / xr) * 100
    itera += 1
    valores.append(xr)
    print(f"{itera:<6} {x_ant:<15.9f} {xr:<15.9f} {fx:<15.9f} {g(xr):<15.9f} {error:<10.3f}")

# --- Resultados ---
print("\n--- RESULTADOS ---")
print(f"xr = {xr:.9f}")
print(f"g(xr) = {g(xr):.9f}")
print(f"error = {error:.9f}%")
print(f"iteraciones = {itera}")

# --- Gráfico ---
xs = [xr - 2 + i*4/200 for i in range(201)]
ys = [g(x) for x in xs]

plt.plot(xs, ys, label=f"g(x)={g_str}")
plt.plot(xs, xs, color='gray', linestyle='--', label="y=x")
plt.scatter(valores, [g(v) for v in valores], color='red', label='Aproximaciones')
plt.title("Método de Punto Fijo")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
