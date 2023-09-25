# REPASO DE PYTHON
## 1. TIPOS DE DATOS. 
> # tipo de datos primitivos. 
> "a" # string  cadena texto
> "hola" # esto tambien es un string
> "hola soy un string y te saludo" # cadena larga
> #### OBSERVACION:todo lo que este entre comillas es un string.
> "100"
> 'false'
> "hola"
> un string puede estar entre comillas simples o dobles
>## tipo numerico
>- 100 este es un tipo de dato numerico entero "integer"
>- 2.1 este es un tipo de datos numerico de flotante "float"
>- false este es un tipo de datos booleano falso true 


## 2. VARIABLES.
> una variable es donde almacenamos nuestro tipo de dat, estos datos pueden mutar cambiar o modificar.
> como creamos una variable para almacenar nuestros datos.
> - darle un nombre significativo o relacionado al dato que estamos almacenhando.
> - Indicarle a que dato esta asociado o relacionado "asignacion '='".
> - Indicar el tipo de dato que se va almacenar -> darle el dato a guardar.
```python
#primero el dato voy a pedir la edad de nadine
edad_ nadine=18
#el nombre de un alunmo
 nombre_alumno="feli"
```

## 3. OPERADORES.
> 1. operdadores aritmeticos.
 - suma +  
 -  resta-
 - multiplicacion *
 - divicion /
 - 
**suma**
```python

suma=15+12
```
**resta**
```python

resta=15-12
```
**multiplicacion**
```python

resta=2*5
```
**divivion**
```python

divi=4/2
```
```python
operacion=(45+12+23)/4
op=15+12+14+13/4
#precedencia de operacion
```
>operadores de uso especial
```python
suma=45+42 # operador suma resultado
suma='45'+12 #operador concatenacion resultado 4512
saludo='hola'+'mundo' # concatenacion holamundo
saludos='hola'+'mundo' # concatenacion hola  mundo
saludos='hola'*2 #holahola
```
## 4. DATOS  ESTRUCTURAL.
>1.listas
[ ]
>
> puedo almacenar distintos tipos de datos en una lista separados por comas.
```python
lista=['nombre',10,false]
lista_amigos=['jory','cristian','adan']
```
>2.objetos 
{ }
>
> tambien al igual que las listas almacenan distintas tipos de datos pero con un orden.
> Para almacenar datos en un objeto necesitamos especificar un indice y un valor clave-> valor
```python
alumno={
    'nombre':'cristian',
    'edad':25,
    'sexo':'masculno'
}
```
> ### se puede combinar ambas estructuras de datos.
```python
alumno={
    'nombre':'cristian',
    'edad':25,
    'sexo':'masculno',
    'amigos':['anthony','edwin','china'],
    'direccion':{
        'departamneto':'ayacucho',
        'provencia':'lucanas',
        'distrito':'puquio',
        'jiron':'san pedro',
        'numwero':125
    }
}
```
## 5. controles de flujos.
> ### 1.decisiones.
> solo se ejecuta el codigo si cumple o si la condicion es verdadera, podemos hacer que si la condicion sea falsa se ejecute otro codigo.
> **sintaxis**
> 
>primero especificar el codigo que se ejecutara si cumple una condicion.
```python
if <condicion>:
    ## el codigo que deseamos ejecutar si la condicion es verdad
    print('ejecuta esto')
    ## aqui estamos fuera del if o del si este codigo siempre  ejecutara no depende del if.
print('esto siempre ejecutara')
#----------------------------------------------------------------------------
# si queremos que se ejecute un codigo en caso sea falso.
if condicion falso>:
    print("SOLO IMPRIME SI ES VERDAD")
else:
    print("solo imprimir si es falso")
```
**ejemplos**
```python
if 15>18:
    print("si es verdadero imprimir esto")
else:
    print("si es falso imprime esto")
```
```python
if 15*2==30:
    print("si es verdadero imprimir esto")
else:
    print("si es falso imprime esto")
```
```python
condicion=True
if condicion:
    print("si es verdadero imprimir esto")
else:
    print("si es falso imprime esto")
```
> ### 2.ciclos.
> existe dos tipos
> cuando sabes la cantidad de veces que vamos a repetir para este caso existe el **for**.
> sintaxis despues de la palabra reservada for deberemos crear una variable que almacene el numero 
> que iremos intentando.
> luego tendremos que indicar el rango a intentar a los elementos a intentar
``` python
 for i in range(1,2)
    print(i)
```
```python
vocales=['a','e','i','o','u']
for i in vocales:
    print(i)
```
```python
numeros=[45,12,78,1,2]
for i in numeros:
    print(i)
```
> cuando no sabemos la cantidad de veces a repetir.

>El uso del **while** nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. Llamaremos iteración a una ejecución completa del bloque de código.
```python
x = 5
while x > 0:
    x -=1
    print(x)

# Salida: 4,3,2,1,0
```
```python
condicion= True
 while True:
    print("hola")
    texto=input('imgrese tu nombre o salir para terminar el programa: ')
    if texto=="sali":
        condicion=false
```

## 6. FUNCIONES.
>   existen dos tipos de funciones
>1. propias de lenguaje.
>
> que ya bienen creadas e insertadas  en python y estan listas para ser usadas.
> estructura de uso de una funcion.
> tiene el nombre seguido de parentesis.
> dentro de parientesispodemos pasarle datos que necesita la funcion para ejecutarse

```python
# esta es una funcion que nos sirve para mostrar por consola datos
print('hola')
```
> **len**
```python
len( )# esta funcion nos permite saber la longitud de una lista o un string 
# len nos devuelve un numero.
print(len([1,2,6,7,8]))
```

**input( )**
>  este es una funcion que se detiene a esperar que el usuario intrudusca la informacion 
>  entre parentesis podremos escribir un mensaje que indique que accion realizara el usuario.
input('ingrese ingresa')


**max** esta funcion nos muuestra el numero mayor de una lista 
```python
lista=[45,12,78,3,24,50]
numero_mayor=max(lista)
print(numero_mayor)
```
**min** esta funcion nos muestra el numero menor de una lista

```python
lista=[45,12,78,3,24,50]
numero_menor=min(lista)
print(numero_menor)
```

**string** funcion para convertir de una string a un numero entero
```python
numero _string='100'
print(type(numero_string))
numero_entero=int(numero_string)
print(type(numero_entro))
```
```python
int('100')#->>100  ->> entero
```
funcion para convertir un entero a un string

```python
str('100')#->> '100'  ->> string
```
> **append** FUNCION DE PYTHON QUE NOS PERMITE AGREGAR ELEMENTOS AL FINAL DE UNA LISTA
```python
lista=[15,12,78]
elemento=100
lista.append(elemento)
print(lista)
```

**pop** funcion de python que nos permite eliminar los elementos que se encuentra al final de la lista
```python
lista=[15,12,78]
lista.pop( )
print(lista)
```

**insert** funcion de python que nos permite agregar elelmentos en cualquier posicion de mi lista para eso 
se le tiene que pasar dos parametros, primero indicarle el indice y segundo el dato que se va agregar
```python
lista_nombre=['jory','nadine','bichota']
lista_nombre.insert(1,'satan')
print(lista_nombre)
```
 **remove** funcion de python que nos permite eliminar elementos de cualquier posicion de una lista, esta funcion 
> recibe solo el elemento que deseamos eliminar.
```python 
lista=[4,5,6,8,6,7]
lista.remove(6)
print(lista)
```
**split** funcion que nos permite dividir en una lista una cadena
```python 
cadena='hola como estas'
lista=cadena.split()
print(lista)
url='www.golle.com/id=70133573'
id_=url.split('=').pop( )
print(id)
```
# 2. funciones creadas o funciones propias
> pasos para crear una funcion propia
>  una funcion son mini programas tambien se le conoce como modulos o fragmentos de codigo de uso exclusiva.
> 1. hacer uso de la palabra reservada def
> 2. definir nombre de funcion que describa que tarea va a realizar
> 3. establercer los parametros que resibira la funcion entre parentesis( )
> 4. establecer que valor odato va retornar mi funcion con la palabra reservada return
>  observacion =>> tambien podemos hacer uso de la funcion print () para retornar un mensaje en nuestra funcion
>  existen dos tipos de funciones los que no resiven ninigun parametro
> y los que resiven parametro 
```python
def saludo():
    print('hola este es un saludo')
```
>  como hacemos uso de la funcion ??
> 
> nombre de la funcion y parentisis
  
  ```python
  def mi_print(texto)
     print(texto)

 print('hola este es print de python')  
 mi_print('hola este es mi print creado')  
  ```
```python
def suma(a,b)
  total=a+b
  return total
  mi_print(suma(45,12)) ##==>>>>  57
```

# ejemplos
> para que se usa esta funcion 
> para mostrar el valor maximo de una lista
``` python
lista=[12,4,45,78,3,1]
mi_print(max(lista)) # ===>>> 78

def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor=numero
    return numero_mayor
mi_print(mi_max(lista))            
```


``` python
lista=[12,4,45,78,3,1]
mi_print(min(lista)) # ===>>> 78

def mi_min(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_menor:
            numero_menor=numero
    return numero_menor
mi_print(mi_min(lista))            
```
# funciones con muchos parametros
```python
def funciones(*muchos_parametros):
    total=0
    for nuemero in muchos_parametros:
        total=total+numero
    return total 
print(funcion(45,12,78,10,20))        
```

```python
def datos(*args):
    nombre=args[0]
    apellidos=args[1]
    edad=args[2]
    return f'mi nombrees,{nombre},{apellidos}y mi edad,{edad}'
print('edwin','apellidos','50')    
```
***cuanto es el factorial de 5
5*4*3*2*1


