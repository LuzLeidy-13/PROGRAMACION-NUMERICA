
# Metodo iterativo ejercicio de supervivencia
set.seed(Sys.time()) # aletioriza cada ejecucion

n_integrantes <- 9  #paremetros
sabores <- c(1, 2, 3)

# Inicialización del grupo
grupo <- data.frame(
  id = 1:n_integrantes,
  dulces = I(lapply(1:n_integrantes, function(i) sample(sabores, 2, replace = TRUE))),
  chupetines = rep(0, n_integrantes)
)

mostrar_estado <- function(iter) {
  cat("\n--- Iteración", iter, "---\n")
  for (i in 1:nrow(grupo)) {
    cat("Integrante", i, 
        "- Dulces:", paste(grupo$dulces[[i]], collapse = ","),
        "| Chupetines:", grupo$chupetines[i], "\n")
  }
}
iter <- 0

repeat {
  iter <- iter + 1
  cat("ITERACIÓN", iter, "\n")
  todos_dulces <- unlist(grupo$dulces)  # Reunir todos los dulces del grupo
  
  # Contar por sabor
  c1 <- sum(todos_dulces == 1)
  c2 <- sum(todos_dulces == 2)
  c3 <- sum(todos_dulces == 3)
  
  cat("Dulces totales en grupo → Sabor1:", c1, "Sabor2:", c2, "Sabor3:", c3, "\n")
  
  # ---- Regla 2: dos grupos de 3 dulces distintos (6 en total)
  grupos6 <- min(c1 %/% 2, c2 %/% 2, c3 %/% 2)
  chupetines <- grupos6 * 2
  dulces_extra <- sample(sabores, grupos6, replace = TRUE)
  
  if (grupos6 > 0)
    cat("se canjearon", grupos6, "grupos de 6 dulces →", chupetines, 
        "chupetines +", grupos6, "dulces extra (", paste(dulces_extra, collapse = ","), ")\n")
  
  # Actualizar inventario
  c1 <- c1 - grupos6 * 2
  c2 <- c2 - grupos6 * 2
  c3 <- c3 - grupos6 * 2
  
  # ---- Regla 1: tres dulces distintos
  grupos3 <- min(c1, c2, c3)
  chupetines <- chupetines + grupos3
  
  if (grupos3 > 0)
    cat("Se canjearon", grupos3, "grupos de 3 dulces distintos →", grupos3, "chupetines\n")
  
  c1 <- c1 - grupos3
  c2 <- c2 - grupos3
  c3 <- c3 - grupos3
  
  dulces_restantes <- c(rep(1, c1), rep(2, c2), rep(3, c3), dulces_extra)  #Combinar dulces restantes
  cat(" Dulces restantes en grupo:", length(dulces_restantes), "\n")
  
  # ---- Distribuir chupetines en grupo (de forma grupal)
  total_chupetines_grupo <- sum(grupo$chupetines) + chupetines
  
  cat(" Chupetines totales acumulados:", total_chupetines_grupo, "\n")
  
  if (total_chupetines_grupo >= n_integrantes) {
    grupo$chupetines <- rep(1, n_integrantes)
    cat("\n Se reunieron los 9 chupetines y se reparten a todos los integrantes \n")
    mostrar_estado(iter)
    break
  } else {
    # Guardar chupetines acumulados (no se reparten aún)
    grupo$chupetines[1] <- total_chupetines_grupo # El primero los custodia
  }
  
  # ---- Repartir dulces sobrantes al azar
  grupo$dulces <- lapply(1:n_integrantes, function(i) {
    if (length(dulces_restantes) >= 2) {
      sample_dulces <- sample(dulces_restantes, 2, replace = FALSE)
      dulces_restantes <<- setdiff(dulces_restantes, sample_dulces)
      sample_dulces
    } else {
      sample(sabores, 2, replace = TRUE)
    }
  })
  
  mostrar_estado(iter)
  
  #  Límite de seguridad para evitar bucles infinitos
  if (iter > 1000) {
    cat("\n Se alcanzó el límite de iteraciones sin conseguir los 9 chupetines.\n")
    break
  }
}