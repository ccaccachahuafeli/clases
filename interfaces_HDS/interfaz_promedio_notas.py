# from tkinter import*
# ventana=Tk()

# def promedio():
#     datos=[]
#     n1=int(a.get())
#     n2=int(b.get())
#     n3=int(c.get())
#     n4=int(d.get())
#     n5=int(e.get())
#     n6=int(f.get())
#     datos.append(n1)
#     datos.append(n2)
#     datos.append(n3)
#     datos.append(n4)
#     datos.append(n5)
#     datos.append(n6)
    
#     suma=n1+n2+n3+n4+n5+n6
#     resultado=suma//len(datos)
#     notas.insert(0,resultado)


# def limpiar():
#     a.delete(0,END)
#     b.delete(0,END)
#     c.delete(0,END)
#     d.delete(0,END)
#     e.delete(0,END)
#     f.delete(0,END)
#     notas.delete(0,END)
#     a.focus()
    
# et=Label(ventana,text='ingresa tu nota en Administracion: ').grid(row=0,column=0)
# a=Entry(ventana)
# a.grid(row=0,column=1)

# et=Label(ventana,text='ingresa tu nota en innovacion: ').grid(row=1,column=0)
# b=Entry(ventana)
# b.grid(row=1,column=1)

# et=Label(ventana,text='ingresa tu nota en Lenguaje: ').grid(row=2,column=0)
# c=Entry(ventana)
# c.grid(row=2,column=1)

# et=Label(ventana,text='ingresa tu nota en Herramientas: ').grid(row=3,column=0)
# d=Entry(ventana)
# d.grid(row=3,column=1)

# et=Label(ventana,text='ingresa tu nota en Metodologia: ').grid(row=4,column=0)
# e=Entry(ventana)
# e.grid(row=4,column=1)

# et=Label(ventana,text='ingresa tu nota enArte: ').grid(row=5,column=0)
# f=Entry(ventana)
# f.grid(row=5,column=1)


# eti=Label(ventana,text='promedio').grid(row=6,column=0)
# notas=Entry(ventana)
# notas.grid(row=6,column=1)

# boton=Button(ventana,text='calcular',command=promedio).grid(row=7,column=0)

# boton_limpiar=Button(ventana,text='Limpiar',command=limpiar).grid(row=7,column=1)


# ventana.mainloop()



from tkinter import *

def calcular_promedio():
    
    nota = float(nota_text.get())
    promedio = (nota + float(E_promedio["text"]))/ 4
    E_promedio["text"]= promedio

def limpiar():
    # Limpiar los campos de nota y promedio
    nota_text.delete(0, "end")
    
def eliminar_todo():
    # Limpiar los campos de nota y promedio
    E_promedio["text"] =0
    nota_text.delete(0, "end")
    
def agregar_nota():
    nota = float(nota_text.get())
    promedio = float(E_promedio["text"]) + nota
    E_promedio["text"]= promedio

# Crear la ventana
ventana = Tk()
ventana.title("♥♦☺")

# Crear las etiquetas
notas=Label(ventana, text="Nota")
notas.grid(row=0, column=0)
nota_text =Entry(ventana)
nota_text.grid(row=0, column=1)

promedio_text =Label(ventana, text="Promedio: ")
promedio_text.grid(row=1, column=0)

E_promedio = Label(ventana, text="0")
E_promedio.grid(row=1, column=1)

# Crear los botones
boton_calcular =Button(ventana, text="Calcular", command=calcular_promedio)
boton_calcular.grid(row=2, column=0)
boton_calcular.config(bg="yellow")

boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=2, column=1)

boton_agregar = Button(ventana, text="+", command=agregar_nota)
boton_agregar.grid(row=0, column=2)

eliminar = Button(ventana, text="Eliminar", command=eliminar_todo)
eliminar.grid(row=4, column=1)
eliminar.config(bg="red")



ventana.mainloop()