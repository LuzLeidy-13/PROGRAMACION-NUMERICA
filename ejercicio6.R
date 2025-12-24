#datos EJERCICIO 6
gasto <- c(0,5,10,15,20,25)
conv <- c(2.1,3.8,5.2,6.1,6.7,7.0)
h <- 5

# Derivadas (margen de conversión por $1k)
marginal <- numeric(length(conv))
marginal[1] <- (conv[2] - conv[1]) / h
for(i in 2:(length(conv)-1)){
  marginal[i] <- (conv[i+1] - conv[i-1]) / (2*h)
}
marginal[length(conv)] <- (conv[length(conv)] - conv[length(conv)-1]) / h

# Segunda derivada en 15k (índice 4)
sec_15k <- (conv[5] - 2*conv[4] + conv[3]) / (h^2)

list(marginal_por_k = marginal, segunda_15k = sec_15k,
     rango_mayor_0_2 = gasto[which(marginal > 0.2)])
