from tkinter import *
root=Tk()
root.geometry("300x300")

framel=LabelFrame(root,text="cuadrito",padx=20,pady=20)  # como funciona padx y pady
framel.config(width=200,height=200)
framel.pack(pady=15)

variable=1
texto=Entry(framel,width=20)
texto.insert(0,str(variable)+"mundo")
texto.pack()

root.mainloop()