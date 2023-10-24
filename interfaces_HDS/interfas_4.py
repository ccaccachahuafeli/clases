# from tkinter import *
# ventana=Tk()
# ventana.title("mi ventana")
# ventana.geometry("500x400")
# # # primero se crea las forma de ventana  como quiero hacer 
# # colum_izquierda=Frame()
# # colum_izquierda.grid(row=0,column=0)
# # colum_izquierda.config(width=200,height=5)
# # etiqueta=Label(ventana,text="esta es el etiqueta")
# # etiqueta.grid(row=0,column=1)
# ventana.mainloop()


from tkinter import *
ventana=Tk()
ventana.title("mi ventana")
ventana.geometry("500x400")
herder=Frame()
herder.grid(row=0,column=1,columnspan=4)
herder.config(width=500,height=15)

aside=Frame()
aside.grid(row=0,column=1,columnspan=4)
aside.config(width=500,height=15)

etiqueta_usuario=Label(ventana)

ventana.mainloop()