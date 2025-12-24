# FUNCIÓN PARA CALCULAR ERROR DE INTERPOLACION
error_interpolacion <- function(x_points, x, Mn1) {
  n <- length(x_points)
  product <- 1
  for (i in 1:n) {
    product <- product * abs(x - x_points[i])
  }
  error <- (Mn1 / factorial(n)) * product
  return(error)
}

# EJERCICIO 1: Error para ln(x)
x_points1 <- c(1, 2, 3)
x1 <- 1.5
Mn1_1 <- 2  # max|f'''(x)| para ln(x) en [1,3]
error1 <- error_interpolacion(x_points1, x1, Mn1_1)
cat("Ejercicio 1 - Error para ln(x) en x=1.5:", error1, "\n")

# EJERCICIO 2: Error para exp(x)
x_points2 <- c(0, 1, 2)
x2 <- 0.5
Mn1_2 <- exp(2)  # max|f'''(x)| para exp(x) en [0,2]
error2 <- error_interpolacion(x_points2, x2, Mn1_2)
cat("Ejercicio 2 - Error para exp(x) en x=0.5:", round(error2, 4), "\n")

# EJERCICIO 3: Error para sin(x)
x_points3 <- c(0, pi/2, pi)
x3 <- pi/4
Mn1_3 <- 1  # max|f'''(x)| para sin(x) en [0,π]
error3 <- error_interpolacion(x_points3, x3, Mn1_3)
cat("Ejercicio 3 - Error para sin(x) en π/4:", round(error3, 4), "\n")

# FUNCIÓN PARA CALCULAR DERIVADAS Y MOSTRAR PASOS
calcular_error_detallado <- function(x_points, x, funcion, intervalo, derivada_orden) {
  n <- length(x_points)
  
  # Calcular producto
  producto <- 1
  cat("Producto: ")
  for (i in 1:n) {
    producto <- producto * abs(x - x_points[i])
    if (i < n) {
      cat("|", x, "-", x_points[i], "| × ")
    } else {
      cat("|", x, "-", x_points[i], "| = ", producto, "\n")
    }
  }
  
  # Calcular error
  error <- (derivada_orden / factorial(n)) * producto
  cat("Error ≤ (", derivada_orden, "/", factorial(n), ") ×", producto, "=", error, "\n")
  
  return(error)
}

# Ejemplo detallado para ln(x)
cat("\n--- CÁLCULO DETALLADO EJERCICIO 1 ---\n")
calcular_error_detallado(c(1, 2, 3), 1.5, "ln(x)", c(1, 3), 2)