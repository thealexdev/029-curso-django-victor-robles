def getNombre(nombre):
    texto = nombre
    return texto


def getApellidos(apellidos):
    texto = apellidos
    return texto


def getFullName(nombre, apellido):
    nombre = getNombre(nombre)
    apellido = getApellidos(apellido)
    nombre_completo = f"El nombre completo es: {nombre} {apellido}"
    return nombre_completo


print(getFullName("Alex", "Hernandez"))
