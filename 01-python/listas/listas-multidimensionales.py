"""
Listas multidimensionales
- son listas que contienen dentro otras listas
"""

contactos = [
    ["Antonio", "antonio@correo.com"],
    ["Luis", "luis@correo.com"],
    ["Andres", "andres@correo.com"],
]

# print(contactos[0][1])

for contacto in contactos:
    nombre = contacto[0]
    correo = contacto[1]
    print(f"Nombre: {nombre}")
    print(f"Correo: {correo}")
