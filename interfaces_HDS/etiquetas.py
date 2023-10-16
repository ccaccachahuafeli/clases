# crear etiquetas
# # impotamos tkinter
# from tkinter import *
# # instanciar la clase Tk()
# ventana=Tk()
# ventana.geometry("400x500")
# # creo mis dos widget de orden inferior con la clase Frame()
# widget_uno=Frame()
# widget_uno.grid(row=0,column=0)
# widget_uno.config(width="400",height="240")
# widget_uno.config(bg="")
# # creacion de etiquetas
# etiqueta=Label(ventana,text="hola soy yo")
# etiqueta.grid(row="0",column="0")
# # usar el metodo mainloop para que la ventana permanezca abierta
# ventana=mainloop()

from tkinter import *

ventana=Tk()
ventana.geometry("400x300")
widget_uno=Frame()
widget_uno.grid(row=0,column=0)
widget_uno.config(width="100",height="100")
etiqueta=Label(ventana,text="ingrese su nombre")
etiqueta.grid(row="1",column="1")
cuadro_texto=Entry()
cuadro_texto.grid(row=1,column=1)
# usar el metodo mainloop para que la ventana permanezca abierta
ventana=mainloop()