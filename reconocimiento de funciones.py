import tkinter as tk
from tkinter import messagebox

def analizar():
    expression = entrada.get().strip()
    
    # 7-9: Validación de entrada
    if expression == "":
        messagebox.showwarning("Error", "Debes ingresar una función matemática.")
        return

    variables = set()
    operaciones = 0

    # 14-27: Bucle para contar variables y operaciones
    for i in range(len(expression)):
        c = expression[i]
        
        # 17-18: Contar variables (letras)
        if c.isalpha():
            variables.add(c)
        
        # 20-21: Contar operadores básicos
        if c in "+-*/^":
            operaciones += 1
            
        # 23-27: Contar operaciones implícitas (ej: '5x' o 'xy')
        if i < len(expression) - 1:
            sig = expression[i+1] # siguiente caracter
            
            # 24-25: Caso '5x' (dígito seguido de letra)
            if c.isdigit() and sig.isalpha(): # # 5x
                operaciones += 1
            
            # 27-28: Caso 'xy' (letra seguida de letra)
            if c.isalpha() and sig.isalpha(): # # xy
                operaciones += 1
    
    # 30-35: Mostrar resultados en la etiqueta
    salida.config(text=
        f"Variables: {', '.join(sorted(variables)) or 'Ninguna'}\n"
        f"N mero de variables: {len(variables)}\n"
        f"N mero de operaciones: {operaciones}")


# 37: ------------------- Interfaz -------------------
ventana = tk.Tk()
ventana.title("Analizador")
ventana.geometry("350x250")

# 42-45: Etiqueta y campo de entrada
tk.Label(ventana, text="Ingresa la función:").pack(pady=5)
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# 46-47: Botón de análisis
tk.Button(ventana, text="Analizar", command=analizar).pack(pady=5)

# 48-50: Etiqueta de salida de resultados
salida = tk.Label(ventana, text="", justify="left")
salida.pack(pady=10)

# 51: Bucle principal de la interfaz
ventana.mainloop()
