# Lista de diccionarios

contactos = [
    {
        "Nombre": "Alejandro",
        "Email": "alex@gmail.com",
    },
    {
        "Nombre": "Beto",
        "Email": "beto@gmail.com",
    },
    {
        "Nombre": "Edgar",
        "Email": "edgar@gmail.com",
    },
]

print(type(contactos))
print(contactos)

# Ingresar a un valor e ingresar a un valor dentro del valor
print(contactos[0]["Email"])

# Cambiar el valor de un diccionario dentro de la lista
contactos[0]["Email"] = "Ejemplo"
print(contactos[0]["Email"])

# Recorrer una lista de diccionarios
for contacto in contactos:
    print(f"Nombre de contacto: {contacto["Nombre"]}")
    print(f"Email de contacto: {contacto["Email"]}")
