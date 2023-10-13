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

# mi_celular = Celular("Samsung", "Galaxy S23", 1000)

# mi_celular.llamar("963258147")
# mi_celular.enviar_mensaje(f"963258147", "Hola, ¿cómo estás?")


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

#     def despegar(self):
#         print("El avión está despegando.")

#     def aterrizar(self):
#         print("El avión está aterrizando.")

#     def obtener_informacion(self):
#         print(f"Modelo: {self.modelo}")
#         print(f"Fabricante: {self.fabricante}")
#         print(f"Capacidad: {self.capacidad} pasajeros")

# mi_avion = Avion("latam 747", "Boeing", 416)

# print(mi_avion.modelo)  
# mi_avion.despegar()     
# mi_avion.aterrizar()    
# mi_avion.obtener_informacion()


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
  

# 5. haciendo el uso de la poo crear un objeto para un pc.

# class pc:
#     def __init__(self, modelo, ram, procesador):
#         self.modelo = modelo
#         self.ram= ram
#         self.procesador= procesador

#     def encendido(self):
#         print("mi pc esta encendiendo.")

#     def actualizar(self):
#         print("mi pc falta actualizar.")

#     def obtener_informacion(self):
#         print(f"Modelo: {self.modelo}")
#         print(f"ram: {self.ram}")
#         print(f"procesador: {self.procesador}")

# mi_pc = pc("22MP58VQ", "kingston 16GB", "intel core i7")

# print(mi_pc.modelo)  
# mi_pc.encendido()     
# mi_pc.actualizar()    
# mi_pc.obtener_informacion()

# 6. haciendo uso de la poo crear un objeto para una impresora

# class impresora:
#     def __init__(self, modelo, marca, memoria_estandar):
#         self.modelo = modelo
#         self.marca= marca
#         self.memoria_estandar= memoria_estandar

#     def impremir(self):
#         print(" impremir a colores.")

#     def scanear(self):
#         print("escania los manuales.")

#     def obtener_informacion(self):
#         print(f"Modelo: {self.modelo}")
#         print(f"marca: {self.marca}")
#         print(f"memoria_estandar: {self.memoria_estandar}")

# la_impresora = impresora("impresora laser", "hp p110", "1MB")

# print(la_impresora.modelo)  
# la_impresora.impremir()     
# la_impresora.scanear()    
# la_impresora.obtener_informacion()


# 7. haciendo uso de la poo crear un objeto para emitir una factura

# class Factura:
#     def __init__(self, numero_factura, cliente, total):
#         self.numero_factura = numero_factura
#         self.cliente = cliente
#         self.total = total

#     def imprimir_factura(self):
#         print("Factura")
#         print("Número de factura:", self.numero_factura)
#         print("Cliente:", self.cliente)
#         print("Total:", self.total)

# mi_factura = Factura("F123", "feliciana Ccaccachahua", 1500)

# print(mi_factura.numero_factura)  
# mi_factura.imprimir_factura()

# 8: crear un objeto clase laptop con dos atributos de clase y 
# 5 atributos de instancia devera tener hasta 3 funcinalidades como minimo
# crear tres objetos instancia de clase distinto 

# class laptop:
#     tipo="pc portatil"
#     tecladoNumero= True
#     def __init__(self,marca,modelo,ram,tipoDisco,almacenamiento):
#         self.marca=marca
#         self.modelo=modelo
#         self.ram=ram
#         self.tipoDisco=tipoDisco
#         self.almacenamiento=almacenamiento
#     def info(self):
#         respueta=f""

# 9. crear una clase puesto de mercado que tenga un atributo de clase ,5 atributos de 
# instancia y 5 funcinalidades.
# dedera crear 4 instancia de la clase mercado 

class PuestoDeMercado:
    # Atributo de clase
    num_puestos = 0

    def __init__(self, nombre, ubicacion, tipo_productos, area, num_empleados):
        # Atributos de instancia
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tipo_productos = tipo_productos
        self.area = area
        self.num_empleados = num_empleados
        PuestoDeMercado.num_puestos += 1

    def mostrar_informacion(self):
        print("Nombre del puesto:", self.nombre)
        print("Ubicación:", self.ubicacion)
        print("Tipo de productos:", self.tipo_productos)
        print("Área:", self.area)
        print("Número de empleados:", self.num_empleados)

    def cambiar_ubicacion(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print("La ubicación del puesto se ha actualizado a:", self.ubicacion)

    def agregar_producto(self, producto):
        self.tipo_productos.append(producto)
        print("Se ha agregado el producto", producto)

    def calcular_area_por_empleado(self):
        area_por_empleado = self.area / self.num_empleados
        print("El área por empleado es:", area_por_empleado)

    @classmethod
    def obtener_num_puestos(cls):
        return cls.num_puestos

# Ejemplo de uso
puesto1 = PuestoDeMercado("Puesto 1", "Centro", ["Frutas", "Verduras"], 50, 2)
puesto1.mostrar_informacion()
puesto1.cambiar_ubicacion("Zona Norte")
puesto1.agregar_producto("Lácteos")
puesto1.calcular_area_por_empleado()

print("Número total de puestos de mercado:", PuestoDeMercado.obtener_num_puestos())
    
        
 

      

        




