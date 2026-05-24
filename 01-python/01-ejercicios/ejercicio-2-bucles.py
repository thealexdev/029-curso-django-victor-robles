"""
Crea un codigo que use un bucle for
para mostrar las tablas de multiplicar que pida un usuario
"""

tabla = int(input("Ingresa la tabla de multiplicar que quieres obtener: "))

numero = 0

if tabla < 1 | tabla > 10:
    print("Esa tabla aun no la puedo hacer, ingresa otra tabla")
else:
    for numero in range(1, 11):
        print(f"{tabla} X {numero} = {tabla * numero}")
20