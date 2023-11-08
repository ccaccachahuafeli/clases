# repaso de programacion  orientado a objetos
# las clases puede generar varios objetos;tienen atributos de clase,atributos de instancia 
# **self** para asociar el metodo con la clase
# _init_ es para ejecutar automaticamente 
# from rich import print
# class Mascota:
#     # atributos de instancia
#     def _init_(self):# self para asociar el methodo con la clase
#         self.nombre=None
#         self.edad=None
#         self.tipo_animal=None
#     # methodos -> funciones o acciones que puede realizar mi clase
#     def hablar(self,sonido):
#         return sonido
#     def datos_mascota(self,nombre,edad,tipo_animal):
#         self.nombre=nombre
#         self.edad=edad
#         self.tipo_animal=tipo_animal

# # instanciar una clase me refiero a crear un objeto
# # como se instancia alamcenando en una variable la clase
# class Perro(Mascota):
#     def atacar(self):
#         return "ladra y muerde"
# class Gato(Mascota):
#     pass

# perro_boby=Perro()
# perro_boby.datos_mascota("boby",14,"perro")
# print(f"[bold blue]"+perro_boby.hablar('guauuu guauu'))
# print("[bold blue]"+perro_boby.atacar())
# print("[bold blue]"+perro_boby.nombre+' '+perro_boby.tipo_animal)


from rich import print

class Persona:
    
    def _init_(self,nombre:str,edad:int,sexo:str):
        self.nombre=nombre
        self.edad=edad
        self.sexoo=sexo
    
    def comen(self,plato_favorito:str):
        return f"yo{self.nombre} estoy comiendo mi {plato_favorito}"
    

    def deporte(self):
        return f"correr,saltar"


class Estudiante(Persona):
    def _init_(self,nombre:str,edad:int,sexo:str,carrera_profesional:str):
     super()._init_(nombre,edad,sexo)
     self.carrera_profesional=carrera_profesional
    def estudiar(self):
      return "estoy estudiando poo"


class Trabajador(Persona):
    def _init_(self, nombre: str, sexo: str, edad: int, dni: int,profesion:str):
        super()._init_(nombre, sexo, edad, dni)
        self.profesion=profesion
    
    def trabajar(self):
        return " estoy en mi trabajo"

jhona=Estudiante("jhonatan henry","masculino",18,71458988,"Arquitectura")
print(f"[bold blue]"+jhona.deporte())
print("[bold blue]"+jhona.come("cebiche"))
print("[bold blue]"+jhona.estudiar())
print("[bold blue]"+jhona.nombre)
