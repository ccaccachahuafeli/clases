# importar mi base de datos
from bd import *        #  la variable usuario de mi bd estara  disponible  en este archivo

#  crear clase para usuario
# esta clase tendra los siguientes metodos
# actualizar edad del usuario
# verificar si usuario  esta registrado  o existe en mis registros
# validar usuario y password
class datos_usuario:

    # def __init__(self, dni,nombre, f_nacimiento,edad, usuario, password):
    #     self.dni = dni
    #     self.nombre = nombre
    #     self.f_nacimiento = f_nacimiento
    #     self.edad = edad
    #     self.usuario = usuario
    #     self.password = password


    def actualizar_edad_usuario(self,dni,f_nacimiento,valor):
        ol=valor
        actualizar_edad_usuario=list(filter(lambda a:a[f_nacimiento]==dni,usuario))[0].update
        ({f_nacimiento:valor})
        return "se actualizo edad"


    def verificar_usuario_registrado(self,):
        pass 


respt=datos_usuario()

print(respt.actualizar_edad_usuario("","f_nacimiento"))