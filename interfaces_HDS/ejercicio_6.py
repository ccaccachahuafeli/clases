from tkinter import *
ventana=Tk() 

ventana.title('OPERADORES')
  
widget_uno=Frame() 
widget_uno.grid(row=6,column=0) 
widget_uno.config(height='30',width='30') 

widget_uno=Frame() 
widget_uno.grid(row=8,column=0) 
widget_uno.config(height='30',width='30')

widget_un=Frame() 
widget_un.grid(row=1,column=1) 
widget_un.config(height='30',width='30')

  
et=Label(ventana,text='Ingresa primer numero :',font=25).grid(row=0,column=0) 
num1=Entry() 
num1.grid(row=1,column=0) 
  
et=Label(ventana,text='Ingresa segundo numero :',font=25).grid(row=2,column=0) 
num2=Entry() 
num2.grid(row=3,column=0) 
  
et=Label(ventana,text='total',font=20).grid(row=4,column=0) 
result=Entry() 
result.grid(row=5,column=0) 
  
class Operadores: 
	def sumar(self):
		n1=int(num1.get())
		n2=int(num2.get())
		sum=n1+n2
		return result.insert(0,sum)
	def restar(self):
		n1=int(num1.get())
		n2=int(num2.get())
		rest=n1-n2
		return result.insert(0,rest)
	def multiplicar(self):
		n1=int(num1.get())
		n2=int(num2.get())
		multi=n1*n2
		return result.insert(0,multi)
	def dividir(self):
		n1=int(num1.get())
		n2=int(num2.get())
		div=n1//n2
		return result.insert(0,div)
		 
		 
datos=IntVar() 
op=Operadores()
def operador():  
    if datos.get()==1: 
        return  (op.sumar())
    if datos.get()==0:
        return (op.restar())
    if datos.get()==2:
        return (op.multiplicar())
    else: 
        return (op.dividir())
            
  
  
radios=Radiobutton(ventana,text='sumar',value=1,variable=datos) 
radios.grid(row=1,column=2) 
  
radior=Radiobutton(ventana,text='restar',value=0,variable=datos) 
radior.grid(row=2,column=2)

radiom=Radiobutton(ventana,text='multiplicar',value=2,variable=datos) 
radiom.grid(row=3,column=2)

radiod=Radiobutton(ventana,text='dividir ',value=3,variable=datos) 
radiod.grid(row=4,column=2) 


boton_calcular=Button(ventana,text='CALCULAR',font=50,command=operador).grid(row=7,column=0)


def limpiar(): 
    num1.delete(0,END) 
    num2.delete(0,END)
    result.delete(0,END)
    num1.focus()
    
def limpiar_resultado(): 
    result.delete(0,END) 
    result.focus()
    
limpiar=Button(ventana,text='LIMPIAR',font=50,command=limpiar).grid(row=7,column=2) 

ventana.mainloop()           



