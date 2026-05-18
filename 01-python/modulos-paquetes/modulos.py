"""
Funcionalidades ya hechas para reutilizar

Podemos conseguir modulos que ya vienen en:
- lenguaje
- internet
- https://docs.python.org/3/py-modindex.html

"""

# importamos el archivo (modulo) que contiene las funciones que nosotros queremos usar
# ? import crearmodulos

# usamos la funcion que nosotros deseamos pero importamos todas las funciones de modulo
# ? print(crearmodulos.hola_mundo("Alejandro"))

# importamos solo la funcion que nosotros queremos
# ? from crearmodulos import hola_mundo

# usamos solo la funcion que nosotros importamos
# ? print(hola_mundo("Alejandro"))

# importamos todas las funciones del modulo explicitamente
from crearmodulos import *

print(hola_mundo("Alejandro"))
