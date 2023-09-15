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
## 6. FUNCIONES.
> 