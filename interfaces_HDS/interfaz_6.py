# radio button
from tkinter import *
# INSTANCIAR-> es crear una variable 
# instanciamos nuestra clase Tk()
ventana=Tk()  #  clase para crear la ventana
ventana.title("clase radiobutton") # haciendo el uso del metodo title para el titulo de mi ventana
ventana.geometry("400x300") # haciendo el uso del metodo  geometria para asignarle un tamaño de la ventana

# instanciar mi clase Label
etiqueta=Label(ventana,text="radio button") # 
# indicar la parte de mi ventana que deseo que se muestre
# puedo usar los metodos grid o pack
etiqueta.config(fg="#3DDB3A",font=50)
etiqueta.pack()

info=IntVar()


def mostrar_radio():
    # respuesta="eres masculino" if info.get()==1 else "eres femenino"
    # etiquetaRespuesta=Label(ventana,text=respuesta)
    # etiquetaRespuesta.pack()
    if info.get()==1:
        etiquetaRespuesta=Label(ventana,text="eres masculino")
        etiquetaRespuesta.pack()

    else:
        etiquetaRespuesta=Label(ventana,text="eres femenino")
        etiquetaRespuesta.pack()    

# instanciar la clase Radiobutton 
radioMasculino=Radiobutton(ventana,text="Masculino",value=1,variable=info)
radioMasculino.pack()

radioFemenino=Radiobutton(ventana,text="Femenino",value=0,variable=info)
radioFemenino.pack()
# INSTANCIAR LA CLASE BUTTON
boton=Button(ventana,text="enviar",command=mostrar_radio)
boton.pack()



# llamar al metodo de Tk que me permite tener persistencia al mostrara la ventana
ventana.mainloop()