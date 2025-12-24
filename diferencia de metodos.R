# =====================================================
# COMPARACIÓN DE RENDIMIENTO ENTRE lm() Y GRADIENTE DESCENDENTE
# =====================================================

# --- Librerías necesarias ---
library(ggplot2)
library(dplyr)
library(bench)
library(patchwork)
library(knitr)
library(profvis)
library(microbenchmark)

# --- Función de Gradiente Descendente para regresión lineal ---
gradiente_descendente <- function(x, y, lr = 0.01, iter = 1000) {
  n <- length(y)
  x <- cbind(1, x)                     # Agregar columna de 1s para el intercepto
  theta <- rep(0, ncol(x))             # Inicialización de parámetros
  
  for (i in 1:iter) {
    pred <- as.vector(x %*% theta)     # Predicción
    grad <- colSums((pred - y) * x) / n
    theta <- theta - lr * grad
  }
  
  return(theta)
}

# --- Función para medir rendimiento ---
evaluar_rendimiento <- function(n) {
  set.seed(123)
  x <- runif(n, 0, 10)
  y <- 5 + 3 * x + rnorm(n, 0, 2)
  datos <- data.frame(x, y)
  
  # --- Método lm() ---
  tiempo_lm <- system.time({
    modelo_lm <- lm(y ~ x, data = datos)
  })
  mem_lm <- bench::mark(lm(y ~ x, data = datos), iterations = 1)$mem_alloc
  
  # --- Método Gradiente Descendente ---
  tiempo_grad <- system.time({
    gradiente_descendente(x, y, lr = 0.001, iter = 2000)
  })
  mem_grad <- bench::mark(gradiente_descendente(x, y, lr = 0.001, iter = 2000), iterations = 1)$mem_alloc
  
  # --- Retornar resultados ---
  data.frame(
    Tamaño = n,
    Método = c("lm", "Gradiente"),
    Tiempo = c(tiempo_lm["elapsed"], tiempo_grad["elapsed"]),
    Memoria_MB = c(as.numeric(mem_lm) / (1024^2), as.numeric(mem_grad) / (1024^2))
  )
}

# --- Evaluar con distintos tamaños ---
tamaños <- c(100, 1000, 5000, 10000, 50000, 100000)
resultados <- do.call(rbind, lapply(tamaños, evaluar_rendimiento))
resultados <- na.omit(resultados)

# --- Mostrar tabla ---
kable(resultados, caption = "Comparación de tiempo y memoria entre lm() y Gradiente Descendente")

# --- Gráfico de tiempo ---
g1 <- ggplot(resultados, aes(x = Tamaño, y = Tiempo, color = Método)) +
  geom_line(linewidth = 1) +
  geom_point(size = 2) +
  theme_minimal(base_size = 14) +
  labs(title = "Comparación de tiempo de ejecución", y = "Tiempo (segundos)", x = "Tamaño de muestra")

# --- Gráfico de memoria ---
g2 <- ggplot(resultados, aes(x = Tamaño, y = Memoria_MB, color = Método)) +
  geom_line(linewidth = 1) +
  geom_point(size = 2) +
  theme_minimal(base_size = 14) +
  labs(title = "Comparación de uso de memoria", y = "Memoria (MB)", x = "Tamaño de muestra")

# --- Mostrar ambos gráficos ---
g1 + g2


# =====================================================
# ANÁLISIS DETALLADO CON MICROBENCHMARK Y PROFVIS
# =====================================================

# --- Microbenchmark (comparación precisa) ---
cat("\n=== MICROBENCHMARK (lm vs Gradiente) ===\n")
microbenchmark(
  lm = lm(y ~ x),
  Gradiente = gradiente_descendente(x, y, lr = 0.001, iter = 2000),
  times = 5
)

# --- Perfilado con Profvis (interactivo) ---
# Ejecuta esta parte solo si quieres abrir la interfaz interactiva
# profvis({
#   gradiente_descendente(x, y, lr = 0.001, iter = 2000)
# })




