"""
Ejercicio #3
Programa que compruebe y realice lo siguiente:

1 - Si una variable esta vacia
2 - Si esta vacia que la rellene con texto en minusculas
3 - Mostrar el contenido de la variable en mayusculas

"""


def programa_tres(valor):
    mensaje_final = "Aún no se evalua nada."
    if valor == None:
        valor = "esto es un texto en minusculas"
        mensaje_final = valor.upper()
    else:
        mensaje_final = f"La variable si tiene contenido, es: '{valor}'."

    return mensaje_final


variable_prueba = None

print(programa_tres(variable_prueba))
