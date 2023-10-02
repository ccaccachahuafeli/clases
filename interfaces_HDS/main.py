# ejemplo practico 
# import tkinter as tk


# ventana = tk.Tk()

# def mostrar_mensaje():
#     etiqueta.config(text="¡Hola, feliciana!")

# boton = tk.Button(ventana, text="Haz clic", command=mostrar_mensaje)
# boton.pack()

# etiqueta = tk.Label(ventana, text="")
# etiqueta.pack()

# ventana.mainloop()


import tkinter as tk


ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("300x200")
def mostrar_mensaje():
    nombre = entrada.get()
    etiqueta.config(text="¡Hola, " + nombre + "!")

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
boton.pack()

ventana.mainloop()