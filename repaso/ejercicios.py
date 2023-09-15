#1. crear un programa que me pida la edad de una persona si la edad es mayor o igual
# a 18 que me muestre un mensaje eres mayor de edad caso contrario que me nuestre un 
# mensaje eres menor de edad.

# nombre=input("ingrese su nombre: ")
# edad=int(input("ingrse su edad: "))
# if edad>=18:
#     print(nombre + "eres mayor de edad")
# else:
#     print(nombre +  "eres menor de edad")


#2. una tienda comercial desea hacer un descuento del 20%,crear un programa que me determine si el 
# cliente se hace  acreedor del descuento teniendo encuenta los siguientes,si el cliente realiza
# una compra de igual o mayor a 1000 solesw mostrar un mensaje que diga 'ganastes el descuento del 20%
# ahora pagaras < mostrar el total de la compra menos el descuento' en caso la compra no supere los 1000 soles
# entonces mostrar un mensaje que diga 'no aplicas al descuento <mostrar el monto de la compra>.

nombre_tienda=("comercial dasaly: ")
nombre_cliente=input("ingrese nombre del cliente: ")
monto_compra=int(input("ingrese el monto de la compra: "))

if monto_compra>=1000:
    descuento=monto_compra*0.2
    total_pagar=monto_compra - descuento
    print("ganastes el descuento del 20%")

else:
    print("no aplicas al descuento de 20%")
    



