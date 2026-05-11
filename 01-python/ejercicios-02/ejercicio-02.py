"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar While y For
"""

cantantes = [1, 5, "Alex"]


def agregar_elementos(lista):

    while len(lista) < 120:
        ingreso = input("Ingresa un valor a la lista: ")
        lista.append(ingreso)

    print("--------------------------------------------")
    print("Los valores de la lista son los siguientes: ")
    print("--------------------------------------------")

    contador = 0
    for elemento in lista:
        contador += 1
        print(f"{contador} ----- {elemento}")

    print("--------------------------------------------")
    print(f"Total de elementos en la lista: {len(lista)}")
    print("Ya has llenado la lista")
    print("--------------------------------------------")

    return contador


numeros = []
for contador in range(118):
    numeros.append(contador)

agregar_elementos(numeros)
