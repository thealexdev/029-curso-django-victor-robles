variable = "Contenido"

# Funsion para imprimir
print(variable)

# Funsion para ver el tipo de dato
print(type(variable))

# Comprobar el tipo de dato
comprobar = isinstance(variable, str)

if comprobar:
    print("Es un string")
else:
    print("No es un string")

# Limpiar espacios
frase = "        mi contenido ___         "
print(frase)
print(frase.strip())  # Funsion que limpia de espacios

# Eliminar variables
year = 2026
print(year)
del year  # Eliminamos una variable
# print(year)

texto = "ff   "
if len(texto) <= 0:
    print("Vacia")
else:
    print("La variable tiene contenido:", len(texto))

# Encontrar caracteres
frase = "La vida"
print(frase.find("vida"))

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "fresa")
print(nueva_frase)

# Mayusculas y minusculas
nombre = "Alejandro"
print(nombre)
print(nombre.lower())
print(nombre.upper())
