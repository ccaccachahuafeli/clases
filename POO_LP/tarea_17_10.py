from tarea_17 import *
class tienda_comercial:

    def tienda_gerente(self,tarea_17_tienda,nombre_gerente):
        respuesta=list(filter(lambda el:el["gerente"]==nombre_gerente,tarea_17_tienda))
        return respuesta
    
    def tienda_mas_categoria(self,tarea_17_tienda):
        respuesta=list(filter(lambda el:len(el["categoria"])>2,tarea_17_tienda))
        return respuesta


    def ruc_nombre(self,tarea_17_tienda):
        respuesta=list(map(lambda par:{"ruc":par["ruc"],"nombre":par["nombre"]},tarea_17_tienda))
        return respuesta
    

    def eliminar_tienda(self,tarea_17,ruc):
        respuesta=list(filter(lambda el:el["ruc"]!=ruc,tarea_17))
        return respuesta
        
# tarea 
    def actualizar_tienda(self):
        pass


    def mostrar_todo(self):
        pass

# otro metodo para crear un nuevo producto
# otro metodo para actualizar el horario de atencion


respuesta1=tienda_comercial() 
# print(respuesta1.tienda_gerente(tienda,"china")) 
# print(respuesta1.tienda_mas_categoria(tienda))
# print(respuesta1.ruc_nombre(tienda))  
print(respuesta1.eliminar_tienda(tienda,1423)) 