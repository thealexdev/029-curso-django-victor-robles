"""
Listas (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre
Para acceder a esos valores podemos usar un indice numerico
"""

# Como se define una lista
peliculas = ["Batman", "Spiderman", "DR Strange"]
print(peliculas)

# Tupla = Datos que no se pueden modificar u actualizar
# list() = Convierte a tipo de dato lista
cantantes = list(("Tupac", "Drake", "Jenifer Lopez"))
print(cantantes)

# Range genera de un numero a un numero, es decir, numero inicial y numero final
years = list(range(2020, 2050))
print(years)

# Lista con diferentes tipos de datos
lista_variada = [2020, "2020", 20.20, ["2020"]]
print(type(lista_variada))
