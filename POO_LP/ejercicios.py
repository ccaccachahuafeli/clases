#1. haciendo uso de la POO crear un objeto para la entidad celular 
# class Celular:
#     def __init__(self, marca, modelo, precio):
#         self.marca = marca
#         self.modelo = modelo
#         self.precio = precio

#     def llamar(self, numero):
#         print(f"Llamando al número {numero} desde un {self.marca} {self.modelo}")

#     def enviar_mensaje(self, numero, mensaje):
#         print(f"Enviando mensaje a {numero} desde un {self.marca} {self.modelo}: {mensaje}")

# # Crear un objeto celular
# mi_celular = Celular("Samsung", "Galaxy S23", 1000)

# # Utilizar métodos del objeto celular
# mi_celular.llamar("963258147")
# mi_celular.enviar_mensaje("963258147", "Hola, ¿cómo estás?")


# 2. haciendo uso de la POO crear un objeto para la entidad vehiculo
# class Vehiculo:
#     def __init__(self, marca, modelo, año):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año

#     def obtener_informacion(self):
#         return f"Vehículo: {self.marca} {self.modelo}, Año: {self.año}"

# 
# mi_vehiculo = Vehiculo("Toyota", "Corolla", 2020)

# print(mi_vehiculo.obtener_informacion())


# 3.haciendo uso de la POO crear un objeto para la entidad avion
# class Avion:
#     def __init__(self, modelo, fabricante, capacidad):
#         self.modelo = modelo
#         self.fabricante = fabricante
#         self.capacidad = capacidad
#         self.en_vuelo = False

#     def despegar(self):
#         if not self.en_vuelo:
#             self.en_vuelo = True
#             print(f"El avión {self.modelo} ha despegado.")
#         else:
#             print(f"El avión {self.modelo} ya está en vuelo.")

#     def aterrizar(self):
#         if self.en_vuelo:
#             self.en_vuelo = False
#             print(f"El avión {self.modelo} ha aterrizado.")
#         else:
#             print(f"El avión {self.modelo} ya está en tierra.")

# # Crear un objeto de la clase Avion
# avion1 = Avion("latam 747", "latam", 416)


# 4. haciendo uso de la POO crear un objeto para un heroe de dota2
# class HeroeDota2:
#     def __init__(self, nombre, tipo, fuerza, agilidad, inteligencia):
#         self.nombre = nombre
#         self.tipo = tipo
#         self.fuerza = fuerza
#         self.agilidad = agilidad
#         self.inteligencia = inteligencia
#         self.vida = 80 
#     def atacar(self):
        
#         pass

#     def usar_habilidad(self, habilidad):
        
#         pass

# mi_heroe = HeroeDota2("lit", "zass", 30, 25, 18)

# print("Nombre del héroe:", mi_heroe.nombre)
# print("Tipo de héroe:", mi_heroe.tipo)
# print("Fuerza del héroe:", mi_heroe.fuerza)
# print("Agilidad del héroe:", mi_heroe.agilidad)
# print("Inteligencia del héroe:", mi_heroe.inteligencia)


