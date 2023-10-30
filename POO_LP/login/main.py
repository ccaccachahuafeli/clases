# importar mi base de datos
#  crear clase para usuario
# esta clase tendra los siguientes metodos
# actualizar edad del usuario
# verificar si usuario  esta registrado  o existe en mis registros
# validar usuario y password
from bd import * # la variable usuario estara disponible en este archivo

class Usuario:

    def __init__(self,dni,nombre, fecha_nacimiento,edad,usuario,password):
        self.dni=dni
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento
        self.edad=edad
        self.usuario=usuario
        self.password=password
    
    
    
    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def ver_usuario(self):
        print("DNI:", self.dni)
        print("Nombre:", self.nombre)
        print("Fecha de nacimiento:", self.fecha_nacimiento)
        print("Edad:", self.edad)
        print("Usuario:", self.usuario)
        print("Contraseña:", self.password)

    def verificar_user(self):
        return self.usuario in usuarios

    def validar_usuario(self, usuario):
        return self.usuario == usuario

    def validar_password(self, password):
        return self.password == password


rpt = Usuario(78954326, "yola", "26/07/1999", '',"estudiante","5555")
rpt.actualizar_edad(24)   
rpt.ver_usuario()
print(rpt.verificar_user())
print(rpt.validar_usuario("estudiante"))
print(rpt.validar_password("5555"))

    