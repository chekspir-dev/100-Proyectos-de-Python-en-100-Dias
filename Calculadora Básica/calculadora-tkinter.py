import tkinter as tk
from tkinter import messagebox


def click_boton(valor):
    if valor == "=":
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except Exception as e:
            messagebox.showerror("Error", "Expresión inválida")
    elif valor == "C":
        entrada.delete(0, tk.END)
    else:
        entrada.insert(tk.END, valor)


ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("360x400")
ventana.resizable(False, False)

entrada = tk.Entry(ventana, font=("Arial", 20), justify="right", bd=10, relief=tk.FLAT)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

fila = 1
columna = 0

for boton in botones:
    accion = lambda valor=boton:click_boton(valor)
    tk.Button(
        ventana, text=boton, width=5, height=2, font=("Arial", 15), command=accion   
          ).grid(row=fila, column=columna, padx=5, pady=5)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

ventana.mainloop()
