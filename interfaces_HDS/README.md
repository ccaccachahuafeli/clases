# averiguar de tkinter
> concepto.
Tkinter es una de las bibliotecas más utilizadas y accesibles para crear aplicaciones gráficas de usuario en Python. En esta serie de artículos, exploraremos cómo crear y personalizar ventanas, widgets (como botones, cajas de texto, menús, etc.) y diálogos con Tkinter. También abordaremos temas avanzados como la manipulación de eventos y la creación de aplicaciones multi-ventana. Con la información que se presentará en estos artículos, estarás en capacidad de crear aplicaciones atractivas y funcionales con Tkinter.

# modo de uso.
1. para utilizar, primero debe importar el modulo en python
```python
import tkinter as tk
```
2. A continuacion, debemos crear una instalacion de la clases**tk** para crear una ventana principal de la aplicacion.
```bash
ventana = tk.Tk()
```
3. Una vez que tienes la ventana principal, se puede agregar diferentes elementosde la interfaz grafica, como botones,etiquetas,cuatros de texto,etc. 
```bash
boton = tk.Button(ventana, text="Haz clic")
boton.pack()
```
4. Finalmente, para iniciar el bucle principal de la aplicacion y mostrar la ventana, se puede llamar al modoto**mainloop()**
```bash
ventana.mainloop()
```