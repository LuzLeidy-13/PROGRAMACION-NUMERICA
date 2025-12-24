# -------------------------------------------------------------
# SIMULACIÓN DEL ERROR DE GRADIENTE BIS VS OTROS MÉTODOS
# -------------------------------------------------------------
if(!require(ggplot2)) install.packages("ggplot2")
library(ggplot2)

# Crear un eje de tiempo
time <- seq(0, 800, by = 10)

# Simulación de curvas (inspiradas en el paper)
classic  <- 2 + 15*(1 - exp(-time/100)) + sin(time/100)*2
flex     <- 2 + 13*(1 - exp(-time/120)) + sin(time/120)*2
crf      <- 2 + 12*(1 - exp(-time/110)) + sin(time/120)*2
bis50    <- 3 + 4*(1 - exp(-time/80))
bisflex50 <- 3 + 4*(1 - exp(-time/90)) + rnorm(length(time), 0, 0.1)
bis90    <- 2 + 1*(1 - exp(-time/60))
bisflex90 <- 2 + 1*(1 - exp(-time/70)) + rnorm(length(time), 0, 0.05)

# Combinar en un data.frame
df <- data.frame(
  time,
  classic,
  flex,
  crf,
  bis50,
  bisflex50,
  bis90,
  bisflex90
)

# Pasar a formato largo para ggplot
library(tidyr)
df_long <- pivot_longer(df, -time, names_to = "method", values_to = "err")

# Colores y estilos similares al paper
colores <- c(
  "classic" = "red",
  "flex" = "blue",
  "crf" = "green3",
  "bis50" = "magenta",
  "bisflex50" = "orange",
  "bis90" = "black",
  "bisflex90" = "grey50"
)

estilos <- c(
  "classic" = "solid",
  "flex" = "longdash",
  "crf" = "dotdash",
  "bis50" = "solid",
  "bisflex50" = "solid",
  "bis90" = "longdash",
  "bisflex90" = "dotted"
)

# -------------------------------------------------------------
# Gráfico tipo paper (curvas de error en el tiempo)
# -------------------------------------------------------------
ggplot(df_long, aes(x = time, y = err, color = method, linetype = method)) +
  geom_line(linewidth = 1.3) +
  scale_color_manual(values = colores) +
  scale_linetype_manual(values = estilos) +
  labs(
    title = expression(paste("space variability = 0.5  and  noise = 1")),
    x = "time", y = "err"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    plot.title = element_text(hjust = 0.5, face = "italic"),
    legend.position = "bottom",
    legend.title = element_blank(),
    legend.background = element_rect(fill = "white", color = "black")
  ) +
  guides(color = guide_legend(nrow = 2))
