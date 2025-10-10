from sympy import *

x = symbols('x')

fun_str = input("Ingrese la función (ejemplo: x**3 - 4*x + 1): ")
fun = sympify(fun_str)
df = diff(fun, x)

x0 = float(input("Ingrese el valor inicial para x: "))
tolerancia = 1e-6
max_iter = 100  # 🔹 Límite de iteraciones

f = lambdify(x, fun)
f_der = lambdify(x, df)

print(f"\nf'(x) = {df}")

error = 1
i = 0

print("\nIter\t x0\t\t x\t\t Error")
print("-" * 50)

while error >= tolerancia and i < max_iter:
    if f_der(x0) == 0:
        print("Error: f'(x) = 0. No se puede continuar con Newton-Raphson.")
        break

    x1 = x0 - f(x0) / f_der(x0)
    error = abs(x1 - x0)
    print(f"{i+1}\t {x0:.6f}\t {x1:.6f}\t {error:.6e}")
    x0 = x1
    i += 1

if i == max_iter:
    print("\n⚠️ El método no convergió en las iteraciones permitidas.")
else:
    print(f"\n Raíz aproximada: {x0:.6f}")
    print(f" Total de iteraciones: {i}")
