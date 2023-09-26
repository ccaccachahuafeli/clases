# ENTORNO VIRTUAL 
>- **VENV** Es la herramienta que permite ver versiones de python; manejador de entorno virtuales ya preinstalado en python.
>- **pienv**  creador de entorno virtual desfasado(ya no se usa)
> - manejador de de paquetes **pip** -> es un comando para poder instalar  paquetes de python para nuestros proyectos.

```python
# para instalar en pip 
pip install <nombre>
```
# para craer un intorno virtual 
> 1.nos ubicamos en la carpeta que deseamos crea el entorno virtual 
```bash
cd <ruta de archivo>
# ejemplo 
cd nombre_carpeta/entorno_uno 
```
> 2. creamos entorno virtual con el seguiente comando
```bash
python -m venv <nombre de nuestro entorno virtual >
# ejemplo
python -m venv mi_entorno
```
> 3. para activar el entorno virtual con el siguiente comando
```bash
source venv/Scrip/activate
```
> #### observacion:
> para poder ejecutar en powershell como terminal predeterminado ejecutar el siguiente comando 
```bash
venv\Script\Activate.ps1
```
## PARA INSTALAR PAQUETES EN NUESTRO ENTORNO VIRTUAL.
> 1. primero verificamos que no tenga paquete instalado y lo listamos con el siguiente comando 
> debemos tener activado nuestro entorno virtual primer.
```bash
pip list
```
>2. luego instalaremos con el siguiente comando.
````bash
pip install <nombre del paquete>
# ejemplo
pip install pandas
```
