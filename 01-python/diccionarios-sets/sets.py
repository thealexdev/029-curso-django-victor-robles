"""
Set es un tipo de dato para tener una coleccion
de valores pero no tiene ni indice ni orden

"""

personas = {"Alex", "Ricardo", "Leonardo"}
print(type(personas))
print(personas)

# metodos

# Agregar
personas.add("Paco")
print(personas)

# Eliminar
personas.remove("Paco")
print(personas)
