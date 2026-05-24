from io import open
from pathlib import Path

ruta = (
    Path(
        r"C:\Users\alexi\OneDrive\Documents\GitHub\cur-django-vr-axv\01-python\sistema-archivos"
    )
    / "nuevo-archivo.txt"
)

# a+ = "Abre el archivo para leer y escribir, y todo lo que escriba agrégalo al final."
archivo = open(ruta, "a+", encoding="utf-8")

archivo.write("Texto insertado\n")

archivo.close()

# Abrir archivo
ruta = (
    Path(
        r"C:\Users\alexi\OneDrive\Documents\GitHub\cur-django-vr-axv\01-python\sistema-archivos"
    )
    / "fichero.txt"
)

# "r" = "Abre el archivo para leerlo"
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# for elemento in contenido:
#     print(elemento)

# Leer contenido y guardar en lista
lista = archivo_lectura.readline()

archivo_lectura.close()

print(lista)
