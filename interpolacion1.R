# EJERCICIO 1: (1,2), (2,4), (3,1)
ejercicio1 <- function() {
  # Definir splines manualmente
  S0 <- function(x) { 2 + (5/3)*(x-1) - (2/3)*(x-1)^3 }
  S1 <- function(x) { 4 - (4/3)*(x-2) - 2*(x-2)^2 + (2/3)*(x-2)^3 }
  
  x_eval <- 2.5
  resultado <- S1(x_eval)
  
  cat("=== EJERCICIO 1 ===\n")
  cat("Datos: (1,2), (2,4), (3,1)\n")
  cat("S(2.5) =", resultado, "\n")
  
  # Verificar con función spline de R
  x_points <- c(1, 2, 3)
  y_points <- c(2, 4, 1)
  spline_r <- spline(x_points, y_points, n = 100)
  idx <- which.min(abs(spline_r$x - x_eval))
  cat("Verificación con spline() de R:", spline_r$y[idx], "\n")
  
  return(resultado)
}

result1 <- ejercicio1()