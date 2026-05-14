"""

Ejercicio #4
Crear un script que tenga 4 variables
- lista
- string
- int
- bool
Que imprima un mensaje segun el tipo de dato de cada variable

"""


#  Funcion que comprueba si una variable es del tipo de dato preguntado
def comprobar_tipado(valor, tipo_dato):
    # Pregunta: Este valor (valor), corresponde a este tipo (tipo_dato)?
    test = isinstance(valor, tipo_dato)
    resultado = ""

    if test:
        resultado = f"Si, es de tipo {type(valor)}"
    else:
        return None

    return resultado


lista = ["Hola Mundo", 77]
titulo = "Alejandro Hernández"
numero = 555
verdadero = True

print(comprobar_tipado(lista, list))
print(comprobar_tipado(titulo, str))
print(comprobar_tipado(numero, int))
print(comprobar_tipado(verdadero, bool))
