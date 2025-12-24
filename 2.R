# datos EJERCICIO 5
horas <- 0:7
lat <- c(120,125,128,135,280,290,275,155)

# Derivada primera
prim <- numeric(length(lat))
prim[1] <- lat[2] - lat[1]
prim[length(lat)] <- lat[length(lat)] - lat[length(lat)-1]
for(i in 2:(length(lat)-1)){
  prim[i] <- (lat[i+1] - lat[i-1]) / 2
}

# Segunda derivada (solo para 2..length-1)
seg <- rep(NA, length(lat))
for(i in 2:(length(lat)-1)){
  seg[i] <- lat[i+1] - 2*lat[i] + lat[i-1]
}

# Salto entre 3 y 4
salto_3_4 <- lat[5] - lat[4]  # indices en R: 4->5 (hora 3->4)

# Tasa de recuperacion 6->7
tasa_recuperacion <- lat[8] - lat[7]

# Anomalías (|delta| > 50)
anomalies <- which(abs(c(prim)) > 50) - 1  # convertir a horas (restar 1 si se quiere ver hora exacta)

list(primera = prim, segunda = seg,
     salto_3_4 = salto_3_4,
     tasa_recuperacion_6_7 = tasa_recuperacion,
     horas_anomalias = anomalies)
