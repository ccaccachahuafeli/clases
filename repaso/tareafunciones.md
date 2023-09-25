# 1. averiguar funciones de python mas usadas, con sus ejemplos practicos.

> **open()**: Abre un archivo para lectura o escritura.
```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
print(contenido)
```
>**join()**: Une una lista de cadenas en una sola cadena.
```python
palabras = ["Hola", "como", "estás"]
texto = " ".join(palabras)
print(texto)
```
> **split()**: Divide una cadena en una lista de subcadenas.

```python
texto = "Hola, como estás"
palabras = texto.split(", ")
print(palabras)
```
> **map()**: Aplica una función a cada elemento de una lista.
```python
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)
```
> **def**: Define una función.
```python
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print("La suma es:", resultado)
```
> **if/elif/else**: Estructuras de control de flujo condicional.
```python
edad = 18
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")

```
> **for loop**: Itera sobre una secuencia.
```python
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)
```
> **append()**: Agrega un elemento a una lista.
```python
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")
print(frutas)
```
> **range()**: Genera una secuencia de números.
```python
numeros = list(range(1, 6))
print(numeros)  # [1, 2, 3, 4, 5]
```
> **len()**: Devuelve la longitud de una secuencia (cadena, lista, tupla, etc.).
```python
palabra = "Python"
longitud = len(palabra)
print("La longitud de la palabra es:", longitud)
```
> **input()**: Lee la entrada del usuario desde la consola.
```python
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")
```
> **print()**: Imprime texto en la consola.
```python
print("Hola, mundo!")
```

# 2. averiguar sobre entornos virtuales en python.

> **¿Qué son los entornos virtuales en Python?** 

Un entorno virtual en Python es una herramienta que te permite crear un ambiente aislado y autónomo para un proyecto específico. Dentro de este ambiente, puedes instalar bibliotecas, dependencias y versiones de Python independientes de las que están instaladas en tu sistema global. Esto ayuda a evitar conflictos entre versiones y dependencias de proyectos diferentes, lo que es especialmente útil cuando trabajas en múltiples proyectos de Python.
# **Ventajas de los entornos virtuales en Python:**
>- **Aislamiento de dependencias:** Cada entorno virtual tiene su propia instalación de Python y sus propias bibliotecas, lo que evita conflictos entre proyectos que requieren versiones diferentes de las mismas bibliotecas.

>- **Facilita la gestión de dependencias:** Puedes instalar y gestionar las dependencias específicas de tu proyecto sin afectar a otras partes de tu sistema.

>- **Versionamiento de Python:** Puedes utilizar diferentes versiones de Python en entornos virtuales, lo que es útil cuando trabajas en proyectos que requieren versiones específicas de Python.

>- **Portabilidad:** Puedes compartir fácilmente un archivo de requisitos (como requirements.txt) que permita a otros replicar tu entorno virtual y ejecutar tu proyecto.

# Bibliotecas populares para gestionar entornos virtuales:

>- **venv:** Es la herramienta estándar para crear entornos virtuales en Python.

>- **virtualenv:** Una alternativa a venv que ofrece más flexibilidad y funcionalidades avanzadas.

>- **conda:** Una herramienta de gestión de paquetes y entornos que se utiliza ampliamente en el ámbito de la ciencia de datos y la inteligencia artificial.

# Cómo crear y gestionar entornos virtuales en Python:

**1.Crear un entorno virtual:**
Usa la herramienta **venv** (disponible en Python 3.3 y versiones posteriores) para crear un entorno virtual. Ejemplo:

> python3 -m venv mi_entorno_virtual

**2.Activar un entorno virtual:**
Para activar un entorno virtual en sistemas Unix/Linux/macOS, utiliza:

> source mi_entorno_virtual/bin/activate **En Windows, utiliza:**
 mi_entorno_virtual\Scripts\activate.

**3.Desactivar un entorno virtual:**
Para salir del entorno virtual y volver al entorno global de Python, simplemente ejecuta:
>deactivate

**4. Instalar paquetes en el entorno virtual:**
Dentro de un entorno virtual activado, usa pip para instalar paquetes específicos para tu proyecto. Ejemplo:
> pip install nombre_del_paquete.

**5.Exportar dependencias a un archivo:**
Puedes generar un archivo de requisitos que enumera las dependencias de tu proyecto usando:
> pip freeze > requirements.txt


**6.Instalar dependencias desde un archivo:**
Para instalar las dependencias desde un archivo de requisitos en otro entorno virtual, usa:
> pip install -r requirements.txt

