"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista
- Hacer funcion que recorrar listas numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

# Creamos la lista
numeros = [1, 5, 3, 4, 2, 6, 7, 8, 9]


def listar_numeros(lista):
    print(f"------------------------------")
    print(f"Los valores desordenados son: ")
    print(f"------------------------------")

    for item in lista:
        print(item)

    print(f"------------------------------")
    print(f"      Ordenamos la lista:     ")
    print(f"------------------------------")

    lista_ordenada = sorted(lista)
    print(lista_ordenada)

    print(f"------------------------------")
    print(f"  La longitud de la lista es: ")
    print(f"------------------------------")

    longitud = len(lista)
    print(longitud)

    user_search = int(input("Ingresa un valor para buscar en la lista: "))

    if user_search in lista:
        print(f"Este valor si se encuentra en la lista: {user_search}")
    else:
        print(f"Este valor no se encuentra en la lista: {user_search}")


listar_numeros(numeros)
