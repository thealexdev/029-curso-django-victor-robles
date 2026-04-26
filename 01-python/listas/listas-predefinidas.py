cantantes = ["Michael Jackson", "Beto Cuevas", "Alex"]
numeros = [1, 2, 8, 4, 3, 6, 7, 5]

# Ordenar una lista
numeros.sort()
print(numeros)

# Agregar elementos
cantantes.append("Wisin y Yandel")
cantantes.insert(4, "David Bisbal")
print(cantantes)

# Eliminar elementos de una lista
cantantes.pop(4)
cantantes.remove("Alex")
print(cantantes)

# Dar la vuelta a una lista
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
cantantes.append("Alex")
print("Alex" in cantantes)

# Contar los elememntos de una lista
print(len(cantantes))

# Cuantas veces aparece un elemento en una lista
numeros.append(2)
print(numeros)
print(numeros.count(2))

# Conseguir un indice de una lista
print(f"El indice del cantante es: {cantantes.index("Alex")}")

# Unir dos listas
cantantes.extend(numeros)
print(cantantes)
