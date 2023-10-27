
# from tkinter import *
# # instanciar la clase TK()
# ventana=Tk()

# widget_uno=Frame()


# widget_uno.grid(row="0",column="0")
# widget_uno.config(width="100",height="100")
# widget_uno.config(bg="green")

# widget_dos=Frame()
# widget_dos.grid(row="0",column="1")
# widget_dos.config(width="100",height="100")
# widget_dos.config(bg="green")

# widget_tres=Frame()
# widget_tres.grid(row="2",column="0")
# widget_tres.config(width="100",height="100")
# widget_tres.config(bg="pink")

# widget_uno.grid(row="2",column="1")
# widget_uno.config(width="100",height="100")
# widget_uno.config(bg="violet")

# widget_dos=Frame()
# widget_dos.grid(row="3",column="0")
# widget_dos.config(width="100",height="100")
# widget_dos.config(bg="orange")

# widget_tres=Frame()
# widget_tres.grid(row="3",column="1")
# widget_tres.config(width="100",height="100")
# widget_tres.config(bg="red")

# ventana.mainloop()


from tkinter import *
# instanciar la clase TK()
ventana=Tk()

widget_uno=Frame()


widget_uno.grid(row="0",rowspan="2",column="0")
widget_uno.config(width="100",height="200")
widget_uno.config(bg="green")

widget_dos=Frame()

widget_dos.grid(row="0",column="1")
widget_dos.config(width="100",height="100")
widget_dos.config(bg="blue")

widget_tres=Frame()

widget_tres.grid(row="1",column="1")
widget_tres.config(width="100",height="100")
widget_tres.config(bg="pink")

Widget_cuatro=Frame()

Widget_cuatro.grid(row="2",column="0",columnspan="2")
Widget_cuatro.config(width="200",height="100")
Widget_cuatro.config(bg="yellow")

ventana.mainloop()