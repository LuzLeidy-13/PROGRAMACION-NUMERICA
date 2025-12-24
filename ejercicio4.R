\subsection*{Código en R}
\begin{lstlisting}[caption={Ejercicio 3 }]
# Datos EJERCICIO 3
dias <- c("Lun","Mar","Mie","Jue","Vie","Sab","Dom")
ventas <- c(45, 52, 61, 58, 73, 89, 95)

# 1) Primera derivada
primera <- numeric(length(ventas))
primera[1] <- ventas[2] - ventas[1]               # adelante
primera[7] <- ventas[7] - ventas[6]               # atrás
for(i in 2:6){
  primera[i] <- (ventas[i+1] - ventas[i-1]) / 2   # centrada
}

# 2) Segunda derivada
segunda <- rep(NA, 7)
for(i in 2:6){
  segunda[i] <- ventas[i+1] - 2*ventas[i] + ventas[i-1]
}

# 3) Caída del jueves
caida_jueves <- ventas[3] - ventas[4]

# 4) Predicción lunes siguiente
pred_lunes <- ventas[7] + primera[7]

primera
segunda
caida_jueves
pred_lunes