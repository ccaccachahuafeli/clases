from tkinter import*
ventana=Tk()

et=Label(ventana,text='numero1').grid(row=0,column=0)
num1=Entry()
num1.grid(row=0,column=1)

et=Label(ventana,text='numero2').grid(row=1,column=0)
num2=Entry()
num2.grid(row=1,column=1)

et=Label(ventana,text='resultado').grid(row=2,column=0)
result=Entry()
result.grid(row=2,column=1)

def suma():
    n1=int(num1.get())
    n2=int(num2.get())
    resultado=n1+n2
    result.insert(0,resultado)
    
boton_suma=Button(ventana,text='Sumar',command=suma).grid(row=3,column=0)


def limpiar():
    num1.delete(0,END)
    num2.delete(0,END)
    result.delete(0,END)
    num1.focus()

boton_limpiar=Button(ventana,text='Limpiar',command=limpiar).grid(row=3,column=1)

ventana.mainloop()