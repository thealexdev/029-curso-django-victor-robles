"""

Capturar excepciones y manejar errores en código susceptible a fallos/errores

"""

try:
    nombre = input("Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, ingresa un nombre valido")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la operación")
