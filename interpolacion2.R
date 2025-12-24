# EJERCICIO 2: (0,1), (1,3), (2,0)
ejercicio2 <- function() {
  # Definir splines manualmente
  S0 <- function(x) { 1 + (7/4)*x - (3/4)*x^3 }
  S1 <- function(x) { 3 - (5/4)*(x-1) - (9/4)*(x-1)^2 + (3/4)*(x-1)^3 }
  
  x_eval <- 1.5
  resultado <- S1(x_eval)
  
  cat("\n=== EJERCICIO 2 ===\n")
  cat("Datos: (0,1), (1,3), (2,0)\n")
  cat("S(1.5) =", resultado, "\n")
  
  # Verificar con función spline de R
  x_points <- c(0, 1, 2)
  y_points <- c(1, 3, 0)
  spline_r <- spline(x_points, y_points, n = 100)
  idx <- which.min(abs(spline_r$x - x_eval))
  cat("Verificación con spline() de R:", spline_r$y[idx], "\n")
  
  return(resultado)
}

result2 <- ejercicio2()