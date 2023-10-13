# importamos tkinter
from tkinter import *
# instanciar la clase TK()
ventana=Tk()
# creo mis dos widget de orden inferior con la clase Frame()
# instanciar mi primer widget
widget_uno=Frame()
# USARA METODO PARA MONTAR EL FRAME
widget_uno.grid(row="0",column="0")
widget_uno.config(width="100",height="100")
widget_uno.config(bg="yellow")
# el metodo grid recibe dos parametros el numero de la clumna y el numerode la fila donde quiero ubicar mi widget
# creacion de segundo widget
widget_dos=Frame()
widget_dos.grid(row="2",column="0")
widget_dos.config(width="100",height="100")
widget_dos.config(bg="purple")
# usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop()