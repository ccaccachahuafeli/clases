from tkinter import *
ventana=Tk()    
ventana.geometry("350x300")

def capturar_datos():
    usuario =usuario.get()
    contraseña = contraseña.get()
    if not usuario or not contraseña:
        error.config(text="Error:usuaruio y contraseña")
    else:
        
        print("Iniciado sesión")


usuario =Label(ventana,text="Usuario:")
usuario.pack()
usuario =Entry(ventana)
usuario.pack()


contraseña =Label(ventana, text="contraseña:")
contraseña.pack()
contraseña =Entry(ventana, show="*")
contraseña.pack()

capturar_datos =Button(ventana, text="Iniciar_sesión", command=capturar_datos)
capturar_datos.pack()

error =Label(ventana, fg="red")
error.pack()


ventana.mainloop()