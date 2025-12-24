# Datos ejercicio 1
mes <- 1:7
usuarios <- c(10, 15, 23, 34, 48, 65, 85)

# 1) Diferencia centrada en mes 4
tasa_mes4 <- (usuarios[5] - usuarios[3]) / 2

# 2) Diferencia hacia adelante en mes 1
tasa_mes1 <- usuarios[2] - usuarios[1]

# 3) Diferencia hacia atras en mes 7
tasa_mes7 <- usuarios[7] - usuarios[6]

# 4) Segunda derivada para meses 2 al 6
segunda_derivada <- usuarios[3:7] - 2*usuarios[2:6] + usuarios[1:5]
mes_aceleracion <- 2:6

# Resultados
tasa_mes4
tasa_mes1
tasa_mes7
data.frame(Mes = mes_aceleracion, Aceleracion = segunda_derivada)

# 5) Interpretación
# Como la segunda derivada es positiva y constante, el crecimiento es acelerado.
cat("\n5. Interpretacion: La startup está creciendo de forma acelerada, ya que cada mes se suman más usuarios que el mes anterior y la segunda derivada es positiva.\n")
