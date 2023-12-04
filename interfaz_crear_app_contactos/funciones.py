from tkinter import *
from tkinter.messagebox import *
import orm
from tablas.Usuarios import Usuarios
db = orm.SQLiteORM("Alumnos")
db.crear_tabla(Usuarios)
def f_limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellidos_texto.delete(0,END)
    ventana.celular_texto.delete(0,END)

    ventana.nombre_texto.focus()

def f_nuevo(ventana):
    nombre=ventana.nombre_texto.get()
    apellidos=ventana.apellidos_texto.get()
    celular=ventana.celular_texto.get()
    showinfo(title="Nuevo",message="nuevo contacto agregado")
    ventana.tabla_datos.insert("",END,text=nombre,values=(apellidos,celular))
    f_limpiar(ventana)
    
def f_eliminar(ventana):
    item_seleccionado = ventana.tabla_datos.selection()
    dato = ventana.tabla_datos.item(item_seleccionado)['text']
    print(item_seleccionado)
    if item_seleccionado:
        ventana.tabla_datos.delete(item_seleccionado)
        db.eliminar('Usuarios',where=f'id= "{dato}"')
        showwarning(title="ELIMINAR",message="Registro elimnado")
        f_limpiar(ventana)
    else:
        print("Selecciona una fila para eliminar.")

def f_actualizar(ventana):
    if ventana.nombre_texto.get()=="":
        showerror(title="SIN DATOS",message=" no hay nada para actualizar")
    else:
        nombre=ventana.nombre_texto.get()
        apellidos=ventana.apellidos_texto.get()
        celular=ventana.celular_texto.get()
        elem_actualizar=ventana.tabla_datos.selection()
        date = ventana.tabla_datos.item(elem_actualizar)['text']
        mensaje=askyesno(title="Actualizar",message="Estas seguro que deseas actualizar")
        if mensaje == True:
            f_limpiar(ventana)
            dato = {
                'Nombre':nombre,
                'Apellido':apellidos,
                'Celular':celular
                }
            ventana.tabla_datos.selection_remove(elem_actualizar)
            db.actualizar('Usuarios',dato,where=f'id={dato}')
            return ventana.tabla_datos.item(elem_actualizar,text=nombre,values=(apellidos,celular))
        else:
            showinfo(title="NO ACTUALIZO",message="No se actualizo ningun registro")
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)

def f_dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    captura_datos=ventana.tabla_datos.item(elem_actualizar)
    mensaje=askyesno(title="ACTUALIZAR",message="Desea actualizar los datos")
    if mensaje == True:
        nombre=captura_datos["text"]
        apellidos=captura_datos["values"][0]
        celular=captura_datos["values"][1]
        ventana.nombre_texto.insert(0,nombre)
        ventana.apellidos_texto.insert(0,apellidos)
        ventana.celular_texto.insert(0,celular)
        ventana.tabla_datos.selection_remove(elem_actualizar)
    else:
        showinfo(title="ACTUALIZAR",message="Ningun registro seleccionado para actualizar")
        ventana.tabla_datos.selection_remove(elem_actualizar)