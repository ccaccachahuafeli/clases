personas=[
    {
        "id":"1",
        "DNI":71930911,
        "nombre":"feliciana",
        "apellido":"ccaccachahua astoyauri",
        "edad":26,
        "talla":1.50,
        "sexo":"femenino",
    }
]

class Alumno:

    def _init_(self,DNI,nombre,apellido,edad,talla,sexo):
        self.DNI=DNI
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.talla=talla
        self.sexo=sexo
    
    def mostrar_alumno(self):
        mensaje=f"""los datos del alumno son: {personas}"""
        return mensaje
    
    def registrar_alumno(self):
        nuevo_id=len(personas)+1
        alumno_nuevo={
            "id":nuevo_id,
            "DNI":self.DNI,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "edad":self.edad,
            "talla":self.talla,
            "sexo":self.sexo
        }
        registro_alumno=personas.append(alumno_nuevo)
        return f"el siguiente alumno se registro  {alumno_nuevo}"
    
    def mostrar_alumno(self,id):
        alumno_buscar=personas[id-1]
        return alumno_buscar
    
    def eliminar_alumno(delf,id):
        alumno_eliminar=personas.pop(id-1)
        return f"el siguiente alumno fue eliminado {alumno_eliminar}"
    
    def actualizar_alumno(self,id):
        pass

Alum=Alumno(74865923,"adan","huamani colorado",19,1.60,"masculino")
print(Alum.registrar_alumno())
print(Alum.mostrar_alumno())
print(Alum.mostrar_alumno(1))
print(Alum.eliminar_alumno(2))
print(Alum.mostrar_alumno())


# crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
# ejemplo:
tienda=[
    {
    "nombre":"el pichilon",
    "categorias":["abarrotes"],
    "horario_atencion":{
        "dia":7am-12m,
        "tarde":2pm-8pm
    }
    "gerente":"nadine"

    }
]
# observacion: las categorias sera 4 :abarotes,farmacia,bodega,restaurante
# observacion: los gerentes solo podran ser los siguientes: edwin,china,christian,nadine
# ## realizar los siguientes ejercicios 
# crear una clase para tiendas que tenga los siguientes metodos o caso de uso 
# 1 crear un metodo que me filtre las tiendas que tiene cada gerente
# 2 crear un metodo que me muestre los n  