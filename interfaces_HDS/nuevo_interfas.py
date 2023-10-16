# 1. importar tkinter -> libreria para la creación de interfaces  grafica 1

# import tkinter as tk 
# root=tk.tk()


from tkinter import *

# la libreria tkinter tiene tres grandes clases para la creacion de interfaces 
# tk()-> el mas usado
# tkk()
# tcl()

# 2. instancia tk() como generador de interfaz grafica 
nueva_ventana=Tk()

# 3. frame es tambien una clase Frame() para crear un frame tengo que primero instanciarlo.
menu_principal=Frame()
# montamos o inicializamos el frame
menu_principal.pack()
# haciendo el uso de metodo configuracion le damos un tamaño
menu_principal.config(width="200",height="200")
# haciendo el uso de metodo configuracion le damos el color
menu_principal.config(bg="green")
# metodo de tk() que mantiene la ejecucion del programa en un bucle
nueva_ventana.mainloop()

