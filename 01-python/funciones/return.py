# Definimos una función
def saludar(nombre):
    # Defino el valor a retornar
    saludo = f"Hola, saludos {nombre}"
    # Lo retorno (entrego el valor)
    return saludo


# Mostramos el valor en terminal
print(saludar("Alejandro Hernández"))

"""
Funcion que se encargue de generar una calculadora
"""


def calculadora(num1, num2, basicas=False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ""

    if basicas == True:
        cadena += "Suman: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena


print(calculadora(4, 2, basicas=False))
