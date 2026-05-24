import os, shutil
from pathlib import Path

# crear una carpeta
ruta = Path(
    r"C:\Users\alexi\OneDrive\Documents\GitHub\cur-django-vr-axv\01-python\sistema-archivos\ruta-nueva\mi_carpeta"
)

# preguntamos si existe la carpeta
if not os.path.isdir(ruta):
    print("No existe la carpeta")
    # creamos la nueva carpeta
    os.mkdir(ruta)
else:
    print("Ya existe el directorio")

# Eliminar una carpeta
print("Eliminando carpeta")
os.rmdir(ruta)
print("Carpeta eliminada")

# Copiar una carpeta
ruta_original = Path(
    r"C:\Users\alexi\OneDrive\Documents\GitHub\cur-django-vr-axv\01-python\sistema-archivos\ruta-nueva"
)
ruta_nueva = Path(
    r"C:\Users\alexi\OneDrive\Documents\GitHub\cur-django-vr-axv\01-python\sistema-archivos\copiando-carpetas\prueba"
)

if not os.path.isdir(ruta_nueva):
    shutil.copytree(ruta_original, ruta_nueva)
    print("La carpeta se creo")
else:
    print("Ya existe la carpeta")

print("Contenido de mi carpeta")
contenido = os.listdir(
    Path(
        r"C:\Users\alexi\OneDrive\Documents\GitHub\cur-django-vr-axv\01-python\sistema-archivos\mi-carpeta"
    )
)

print(contenido)

for archivo in contenido:
    print("Archivo: ", archivo)
