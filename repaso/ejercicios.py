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

# nombre_tienda=("comercial dasaly: ")
# nombre_cliente=input("ingrese nombre del cliente: ")
# monto_compra=int(input("ingrese el monto de la compra: "))

# if monto_compra>=1000:
# descuento=monto_compra*0.2
#     total_pagar=monto_compra - descuento
#     print("ganastes el descuento del 20%")

# else:
  #  print("no aplicas al descuento de 20%")
    

# 3. crear un programa que me pida 5 veces un  nombre y por cada vez que lo pida muestre
#  la cantidad de veces que ingrese el nombre.
# for n in range(1,6)
#  nombre=input('ingrese su nombre: ')
#  print(f'ingrese {n} veces el nombre')

# 4. crear un programa que pida un numero y lo evalue con el numero premiado  si el 
# numero ingresado es el premiado el programa finalizara si el numero ingresado 
# es incorrecto el programa seguira pidiendo el numero premiado.


# numero_ganador=90
# condicion=True
# while condicion:
#     numero_ingrese=int(input('ingrese un numero: '))
#     if numero_ingrese==numero_ganador:
#         print('ganaste')
#         condicion=False 

# else:
#     print('sigue intentando')



# 5. craer una funcion por cada operador aritmetico que  resiva dos parametros y retorne el resultado
# de la operacion, ojo. crear una funcion que nos permite impremir el resultado.

# def mi_print(texto):
#     print(texto)

# def suma(a,b):
#     return a+b    

# def resta(a,b):
#     return a-b 

# def multi(a,b):
#     return a*b 

# def divi(a,b):
#     return a/b 

# mi_print(suma(8,5))
# mi_print(resta(8,5))
# mi_print(multi(8,5))
# mi_print(divi(8,5))

# 6. escriba una funcion que reciba un numero entero positivo y devuelve su factorial


# def factorial(num):
#     if num==10:
#         return 1
#     else:
#         return num*factorial(num+1)
    
# print(factorial(8))


# def funcion(valor):
#     factorial=1
#     for i in range(valor):
#         factorial *= i+1
#     return factorial


# print(funcion(5))

# 7. escribir una funcion que resiva como parametros una lista de numeros y retorne una nueva 
# lista con cada numero elevados al cuadrado.

# def elevar_al_cuadrado(lista_numeros):
    
#     resultado = []
    
#     for numero in lista_numeros:
#         resultado.append(numero ** 2)
    
#     return resultado

# numeros = [1, 2, 3, 4, 5]
# resultado = elevar_al_cuadrado(numeros)
# print(resultado)  


# 8. escriba un programa que reciba una cadena de caracteres y devuelva un objeto con cada 
#palabra que tiene su frecuencia 

def contar_palabras(cadena):
    palabras = cadena.split()
    
    frecuencia_palabras = {}
    
    for palabra in palabras:
       
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            
            frecuencia_palabras[palabra] = 1
    
    return frecuencia_palabras

texto = input("Ingrese una palabra: ")

frecuencias = contar_palabras(texto)

for palabra, frecuencia in frecuencias.items():
    print(f"{palabra}: {frecuencia}")


