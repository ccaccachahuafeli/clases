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

widget_dos=Frame()
widget_dos.grid(row="0",column="0")
widget_dos.config(width="100",height="100")
widget_dos.config(bg="orange")

widget_tres=Frame()
widget_tres.grid(row="2",column="0")
widget_tres.config(width="100",height="100")
widget_tres.config(bg="red")

# widget_cuatro=Frame()
# widget_cuatro.grid(row="2",column="0")
# widget_cuatro.config(width="100",height="100")
# widget_cuatro.config(bg="purple")

# widget_cinco=Frame()
# widget_cinco.grid(row="2",column="0")
# widget_cinco.config(width="100",height="100")
# widget_cinco.config(bg="purple")

# widget_seis=Frame()
# widget_seis.grid(row="2",column="0")
# widget_seis.config(width="100",height="100")
# widget_seis.config(bg="purple")

# widget_siete=Frame()
# widget_siete.grid(row="2",column="0")
# widget_siete.config(width="100",height="100")
# widget_siete.config(bg="purple")

# widget_ocho=Frame()
# widget_ocho.grid(row="2",column="0")
# widget_ocho.config(width="100",height="100")
# widget_ocho.config(bg="purple")


# usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop()