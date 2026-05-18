"""
1 - Crear el archivo con el nombre que queramos
2 - Crear las funciones que queramos
"""


def hola_mundo(mensaje):
    return mensaje


def calculadora(operacion, num1, num2):
    print("Elije la operacion a realizar:")
    print("SUMA = 1")
    print("RESTA = 2")
    print("MULTIPLICACION = 3")
    print("DIVICION = 4")
    resultado = 0
    if operacion == 1:
        resultado = num1 + num2
    elif operacion == 2:
        resultado = num1 - num2
    elif operacion == 3:
        resultado = num1 * num2
    elif operacion == 4:
        resultado = num1 / num2

    return resultado
