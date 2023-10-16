from tkinter import *


ventana=Tk()


widget_uno=Frame()
widget_uno.grid(row=1,column=1)
name_label =Label(ventana, text="Nombre y apellidos :")
name_entry =Entry(ventana)
widget_uno.config(width="50",height="50")
name_label.grid(row=1, column=1)
name_entry.grid(row=1, column=2)

widget_uno=Frame()
widget_uno.grid(row=2,column=1)
name_label =Label(ventana, text="DNI :")
name_entry =Entry(ventana)
widget_uno.config(width="50",height="50")
name_label.grid(row=2, column=1)
name_entry.grid(row=2, column=2)

widget_uno=Frame()
widget_uno.grid(row=3,column=1)
name_label =Label(ventana, text="celular :")
name_entry =Entry(ventana)
widget_uno.config(width="50",height="50")
name_label.grid(row=3, column=1)
name_entry.grid(row=3, column=2)


widget_uno=Frame()


widget_uno.grid(row="4",rowspan="2",column="1",columnspan="2")
widget_uno.config(width="250",height="200")
widget_uno.config(bg="white")

# cuadro_texto.grid(row=1,column=1)

ventana=mainloop()

