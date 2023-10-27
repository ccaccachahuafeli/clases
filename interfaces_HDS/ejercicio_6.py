from tkinter import *
ventana=Tk()    
ventana.geometry("350x300")

def capturar_numeros():
    usuario =usuario.get()
    contraseña = contraseña.get()



numero1 =Label(ventana,text="ingrese un numero")
numero1.pack()
numero1 =Entry(ventana)
numero1.pack()


numero2 =Label(ventana, text="ingrese un numero")
numero2.pack()
numero2 =Entry(ventana)
numero2.pack()

total =Label(ventana, text="total")
total.pack()
total =Entry(ventana)
total.pack()


capturar_datos =Button(ventana, text="calcular", command=capturar_numeros)
capturar_datos.pack()


def suma():
    n1=int(numero1.get())
    n2=int(numero2.get())
    resultado=n1+n2
    resultado.insert(0,resultado)
    
boton_suma=Button(ventana,text='Sumar',command=suma).grid(row=3,column=0)

ventana.mainloop()