from tkinter import *
ventana=Tk()    # clase
ventana.geometry("350x300") # metodos geometria
ventana.title("ventana suma")  # metodo de nombre

def captura_dato():
     text=text_nombre.get()
     mensaje=Label(ventana,text=f"hola,{text}")
     mensaje.pack()

etiqueta=Label(ventana,text="ingrese su nombre") 
etiqueta.pack()                        
text_nombre=Entry(ventana,relief="solid",borderwidth=2)
text_nombre=Entry(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
text_nombre.config(bg="blue",fg="yellow")
text_nombre.pack()

boton_capturar=Button(ventana,text="enviar",command=captura_dato)
boton_capturar.pack()



ventana.mainloop()    






