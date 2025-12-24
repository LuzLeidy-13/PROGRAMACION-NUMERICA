# GRADIENTE (2 VARIABLES)
library(ggplot2)
library(plotly)

#  Parámetros
n <- 0.1                # Tasa de aprendizaje
x0 <- 3                 # Valor inicial de x
y0 <- 2                # Valor inicial de y
iter <- 25              # Número de iteraciones

# Definición de funciones 
f <- function(x, y) x^2 + y^2                  # Función objetivo
grad_f <- function(x, y) c(2*x, 2*y)           # Gradiente ∇f(x, y)

# Inicialización 
x <- numeric(iter)
y <- numeric(iter)
fx <- numeric(iter)

x[1] <- x0
y[1] <- y0
fx[1] <- f(x[1], y[1])

# Iteraciones del gradiente 
for (i in 1:(iter - 1)) {
  grad <- grad_f(x[i], y[i])
  x[i + 1] <- x[i] - n * grad[1]
  y[i + 1] <- y[i] - n * grad[2]
  fx[i + 1] <- f(x[i + 1], y[i + 1])
}

# Tabla de resultados 
tabla <- data.frame(
  Iter = 1:iter,
  x = x,
  y = y,
  fxy = fx
)
print(tabla)

# Superficie 3D con trayectoria 
x_seq <- seq(-4, 4, length.out = 100)
y_seq <- seq(-4, 4, length.out = 100)
z <- outer(x_seq, y_seq, f)

fig <- plot_ly() |>
  add_surface(x = ~x_seq, y = ~y_seq, z = ~z, opacity = 0.7, colorscale = "Viridis") |>
  add_trace(x = x, y = y, z = fx, type = "scatter3d", mode = "lines+markers",
            line = list(color = "red", width = 5),
            marker = list(size = 3, color = "red"),
            name = "Trayectoria del gradiente") |>
  layout(
    title = "Descenso del Gradiente - f(x, y) = x² + y²",
    scene = list(
      xaxis = list(title = "x"),
      yaxis = list(title = "y"),
      zaxis = list(title = "f(x, y)")
    )
  )

fig

