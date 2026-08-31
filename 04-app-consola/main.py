"""
Proyecto Python y MySQL

- Abrir asistente
- Login o Registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos logn, identificara al usuario y nos preguntara
- Crear nota, mostrar notas, borrar nota

"""

print(
    """
Acciones disponibles:
    - regisrto = 0
    - login    = 1

"""
)

accion = int(input("Que quieres hacer?: "))

if accion == 0:
    print("Vamos a realizar el registro")
elif accion == 1:
    print("Ingresa tus credenciales para continuar")
