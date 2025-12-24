# OPTIMIZACIN WEB POR GRADIENTE (R)


# Sensibilidades (w) - derivadas parciales estimadas
# w = impacto en ms por unidad (KB o request)
w <- c(
  w_img = 6,   # imagenes
  w_js  = 10,  # JavaScript
  w_css = 4,   # CSS
  w_req = 80   # numero de peticiones
)

# Estado inicial x0:
# [imagenes_KB, js_KB, css_KB, requests]
x <- c(
  img = 1500,
  js  = 400,
  css = 200,
  req = 35
)

# Tiempo inicial observado (PageSpeed/JMeter)
T0 <- 8690

# Tasas de aprendizaje (alpha) por variable
alpha <- c(
  img = 0.5,
  js  = 0.2,
  css = 0.5,
  req = 0.01
)

# Funcion del modelo (forma lineal)
f <- function(x, w) {
  sum(w * x)
}

# Iteraciones del gradiente
max_iter <- 10

cat("==== Descenso del Gradiente ====\n")
cat("Iter | Imagenes | JS | CSS | Req | Tiempo Estimado\n")
cat("---------------------------------------------------\n")

for (i in 1:max_iter) {
  
  grad <- w            # el gradiente es constante en este modelo
  dx <- alpha * grad   # paso de actualizacion
  x <- x - dx          # nuevo punto
  
  T_est <- f(x, w)
  
  cat(sprintf("%4d | %8.2f | %6.2f | %6.2f | %5.2f | %10.2f ms\n",
              i, x[1], x[2], x[3], x[4], T_est))
}

cat("---------------------------------------------------\n")
cat("Optimizacion completada.\n")