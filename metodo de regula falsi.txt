import math, re, matplotlib.pyplot as plt

print("=== MÉTODO DE REGULA FALSI ===")

def preparar_funcion(expr):
    expr = expr.lower().strip()
    expr = expr.replace("^", "**").replace("sen", "sin").replace("ln", "log").replace("π", "pi")
    expr = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z\)])(\d)', r'\1*\2', expr)
    return expr

funcion_str = input("Ingrese la función f(x): ")
funcion_str = preparar_funcion(funcion_str)

def f(x):
    try: return eval(funcion_str, {"__builtins__": None}, math.__dict__ | {"x": x})
    except: return None

x1 = float(input("Ingrese x1 = "))
x2 = float(input("Ingrese x2 = "))
f1, f2 = f(x1), f(x2)
if f1 * f2 > 0:
    print("No hay cambio de signo entre x1 y x2.")
    exit()

tol, max_iter = 1e-10, 100
itera, error, xr = 0, 1, x1
valores = []

print(f"\n{'Itera':<6} {'xr':<15} {'error':<15} {'f(xr)':<15}")
print("-" * 55)

while itera < max_iter and error > tol:
    xant = xr
    xr = x2 - f2 * (x1 - x2) / (f1 - f2)
    fxr = f(xr)
    if fxr is None: break
    itera += 1
    error = abs(xr - xant)
    valores.append(xr)
    print(f"{itera:<6} {xr:<15.10f} {error:<15.10f} {fxr:<15.10f}")
    if f1 * fxr < 0:
        x2, f2 = xr, fxr
    else:
        x1, f1 = xr, fxr

print("\n--- RESULTADOS ---")
print(f"xr = {xr:.10f}")
print(f"f(xr) = {f(xr):.10f}")
print(f"error = {error:.10f}")
print(f"iteraciones = {itera}")

# --- GRAFICAR ---
xs = [x1 + i*(x2-x1)/200 for i in range(201)]
ys = [f(x) for x in xs]
plt.plot(xs, ys, label="f(x)")
plt.axhline(0, color='black')
plt.scatter(valores, [f(v) for v in valores], color='red', label='Aproximaciones')
plt.title("Método de Regula Falsi")
plt.legend()
plt.show()
