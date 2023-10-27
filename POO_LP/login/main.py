# importar mi base de datos
from bd import *        #  la variable usuario de mi bd estara  disponible  en este archivo

#  crear clase para usuario
# esta clase tendra los siguientes metodos
# actualizar edad del usuario
# verificar si usuario  esta registrado  o existe en mis registros
# validar usuario y password

from bd import *

class User:
    def mostrar_usuario(self, ide):
        resultado=list(filter(lambda par:par["DNI"]==ide,usuario))
        return f"""Aqui tienes informacion de la usuario que buscaste:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& 
        {resultado}
"""
    
    def agregar_edad(self, clave, valor):
        for usuario in usuario:
            if usuario["DNI"] == clave:
                usuario[clave] = valor
                return "Se actualizó."
        return "Usuario no encontrado."

# verificar si usuario esta registrado o existe en mis registros
    def verificar_usuario(self, usuario_buscar):
        for usuario in usuario:
            if usuario["Usuario"] == usuario_buscar:
                return "Usuario registrado."
        return "Usuario no encontrado en los registros."

# validar usuario y password
    def validar_usuario_password(self, usuario_a_validar, password_a_validar):
        for usuario in usuario:
            if usuario["Usuario"] == usuario_a_validar and usuario["Password"] == password_a_validar:
                return "Usuario y contraseña válidos."
        return "Usuario o contraseña incorrectos."

rpt=User()
print(rpt.agregar_edad("edad", 17))
print(rpt.mostrar_usuario(7645343))

usuario_a_buscar = "rodriguesC"
print(rpt.verificar_usuario(usuario_a_buscar))
print(rpt.mostrar_usuario(74930911))

usuario_a_validar = "rodriguesC"
password_a_validar = "1325"
print(rpt.validar_usuario_password(usuario_a_validar, password_a_validar))
print(rpt.mostrar_usuario(7645986))