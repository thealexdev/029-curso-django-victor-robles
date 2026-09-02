"""
Proyecto Python y MySQL

- Abrir asistente
- Login o Registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos logn, identificara al usuario y nos preguntara
- Crear nota, mostrar notas, borrar nota

"""

from usuarios import acciones


print(
    """
Acciones disponibles:
    - regisrto = 0
    - login    = 1

"""
)

hazEl = acciones.Acciones()

accion = int(input("Que quieres hacer?: "))

if accion == 0:
    hazEl.registro()
elif accion == 1:
    hazEl.login()
