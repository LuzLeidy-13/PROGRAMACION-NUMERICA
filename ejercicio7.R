#datos EJERCICIO 7
tiempo <- 0:7
temp <- c(20.1,20.3,20.8,21.5,22.6,24.2,26.1,28.5)

# 1) Primera derivada (velocidad)
vel <- numeric(length(temp))
vel[1] <- temp[2] - temp[1]     # adelante
for(i in 2:(length(temp)-1)){
  vel[i] <- (temp[i+1] - temp[i-1]) / 2
}
vel[length(temp)] <- temp[length(temp)] - temp[length(temp)-1]  # atras

# 2) Segunda derivada (aceleracion) para 1..6
acel <- rep(NA, length(temp))
for(i in 2:(length(temp)-1)){
  acel[i] <- temp[i+1] - 2*temp[i] + temp[i-1]
}

# 3) Detectar alertas (> 0.8 °C/s)
alertas <- which(vel > 0.8) - 1  # restar 1 si quieres indices inicio en 0 para tiempo

# 4) Normalizar (min-max) las features (excluyendo NA)
vel_non_na <- vel[!is.na(vel)]
acel_non_na <- acel[!is.na(acel)]

norm <- function(x){ (x - min(x)) / (max(x) - min(x)) }

vel_norm <- norm(vel_non_na)
acel_norm <- norm(acel_non_na)

list(velocidad = vel, aceleracion = acel,
     tiempos_alerta = alertas,
     vel_norm = vel_norm, acel_norm = acel_norm)

