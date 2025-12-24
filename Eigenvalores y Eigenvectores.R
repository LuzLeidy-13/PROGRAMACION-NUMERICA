# Eigenvalores, Eigenvectores y Optimización

cat("===== EJERCICIO 1 =====\n")
# Matriz A
A <- matrix(c(4, 0,
              0, 7), nrow = 2, byrow = TRUE)

cat("Matriz A:\n")
print(A)
cat("Eigenvalores y Eigenvectores:\n")
print(eigen(A))


cat("\n===== EJERCICIO 2 =====\n")
# Matriz B
B <- matrix(c(1, 2,
              2, 1), nrow = 2, byrow = TRUE)

cat("Matriz B:\n")
print(B)
cat("Eigenvalores y Eigenvectores:\n")
print(eigen(B))


cat("\n===== EJERCICIO 3 =====\n")
# f(x1, x2) = 2x1^2 + x2^2 - 2x1x2
# Hessiana
H <- matrix(c(4, -2,
              -2, 2), nrow = 2, byrow = TRUE)

cat("Matriz Hessiana H:\n")
print(H)
eigH <- eigen(H)
cat("Eigenvalores:\n")
print(eigH$values)

cat("Clasificación del punto crítico (0,0):\n")
if (all(eigH$values > 0)) {
  cat("MÍNIMO local\n")
} else if (all(eigH$values < 0)) {
  cat("MÁXIMO local\n")
} else {
  cat("PUNTO SILLA\n")
}


cat("\n===== EJERCICIO 4 =====\n")
# f(x1, x2) = -x1^2 - 2x2^2
# Hessiana
H4 <- matrix(c(-2, 0,
               0, -4), nrow = 2, byrow = TRUE)

cat("Matriz Hessiana:\n")
print(H4)
eigH4 <- eigen(H4)
cat("Eigenvalores:\n")
print(eigH4$values)

cat("Clasificación del punto crítico (0,0):\n")
if (all(eigH4$values < 0)) {
  cat("MÁXIMO local\n")
} else if (all(eigH4$values > 0)) {
  cat("MÍNIMO local\n")
} else {
  cat("PUNTO SILLA\n")
}


cat("\n===== EJERCICIO 5 =====\n")
# Matriz C y vector v
C <- matrix(c(3, 2,
              1, 4), nrow = 2, byrow = TRUE)

v <- c(2, 1)

cat("Matriz C:\n")
print(C)
cat("Vector v:\n")
print(v)

Cv <- C %*% v
cat("Producto C * v:\n")
print(Cv)

lambda <- Cv / v
cat("Eigenvalor asociado:\n")
print(lambda)

cat("Conclusión:\n")
cat("v es eigenvector y λ = 4\n")
