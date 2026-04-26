"""
Diccionarios =
Conjunto de valores, en lugar de indices numericos, son indices alfa numericos
Formato clave valor
Parecido a un array asociativo o un JSON si vienes de JS
"""

persona = {
    "Nombre": "Alejandro",
    "Apellidos": "Hernandez",
    "Edad": 18,
    "Ciudad": "Puebla",
}

print(type(persona))
print(persona["Apellidos"])  # Accedemos a un valor en especifico
