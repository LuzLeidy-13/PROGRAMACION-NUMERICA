# Datos
epoca <- c(0, 10, 20, 30, 40, 50)
loss <- c(2.45, 1.82, 1.35, 1.08, 0.95, 0.89)

# 1) Derivada centrada en epoca 20
tasa_20 <- (loss[4] - loss[2]) / (2*10)

# 2) Segunda derivada en epoca 30
segunda_30 <- (loss[5] - 2*loss[4] + loss[3]) / (10^2)

# 3) Buscar cuando la tasa de cambio < 0.01 por época
tasas <- diff(loss) / 10
epoca_detener <- epoca[-1][tasas < 0.01][1]

# 4) Interpolacion lineal para época 25
pendiente <- (loss[4] - loss[3]) / 10
loss_25 <- loss[3] + pendiente * 5

tasa_20
segunda_30
epoca_detener
loss_25