# crear un sistema para gestion control de stock de producto
# entidad 
# la base de datos sobre la que voy a trabajar 
# averiguar formas normales (normalizacion de base de datos)
productos=[
    {
        "ID":1,
        "codigo":"2023-A",
        "nombre":"arroz",
        "descripcion":"costeño costal x 100 k",
        "stock":5,
        "unidad":"costales",
        "precio":125,
        "moneda":"soles"

    }
]

#casos de uso
class Producto:

    #atributos de instancia:
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda

    #creacion de metodos:
    def mostrar_productos(self):
        mensaje=f"""
    Tienes {len(productos)} productos
    Los productos son: 
    {productos}
"""
        return mensaje
        
    def registrar_producto(self):
        nuevo_id=len(productos)+1
        codigo="2023-B"
        producto_nuevo={
            'id': nuevo_id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'stock': self.stock,
            'unidad':self.unidad,
            'precio': self.precio,
            'moneda':self.moneda

        }
        registro_producto=productos.append(producto_nuevo)
        return f"el siguiente producto se registro exitosamente {producto_nuevo}"
    
    def mostrar_un_producto(self,id):
        producto_buscar=productos[id-1]
        return producto_buscar
    
    def eliminar_producto(self,id):
        producto_eliminado=productos.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminado}"

    def actualizar_producto(self,id,clave,valor):
        ol=valor
        producto_actualizar=list(filter(lambda el: el[clave]==id,productos))[0].update
        ({clave:valor})
        return "se actualizo"


   # lista funcion para crear
   # PROGRAMACION funional en python
   # metodo funcional filter retornar una lista con el elemento que se 
   # funciones anonimas o autoejecutadas en python se les conoce como funciones 
   # lambda funcion anonima
   # su uso estructural 
   # lambda a,b:retur a+b  ->   esta funcion se autoejecuta no se llama
   # suma= lambda a,b:retun a+b-> para ejecutar esta funcion necesito llamar a la variable suma
   # suma(3,4)

        
prod=Producto('aceite','sol 1L',2,'BOTELLA',10)
print(prod.registrar_producto())
print(prod.mostrar_productos())
print(prod.actualizar_producto(125,"precio",130))
print(prod.mostrar_productos)