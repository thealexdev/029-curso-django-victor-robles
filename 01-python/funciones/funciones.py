"""
Funciones:
Conjunto de instrucciones agrupabas bajo un nombre que
pueden reutilizarse todas las veces que se "llamen" o "usen"

ejemplo:
def nombreFuncion(parametros):
    bloque de codigo
    conjunto de instrucciones


nombreFuncion(parametros)

Ejemplo:
def sumar(num1, num2):
    res = f"La respuesta es: {num1 + num2}"
    print(res)

sumar(1, 5)

"""


def muestraNombre(num):
    if num == 1:
        print("Alejandro")
    else:
        print("No me diste una opcion")


muestraNombre(0)
muestraNombre(1)
muestraNombre(0)
