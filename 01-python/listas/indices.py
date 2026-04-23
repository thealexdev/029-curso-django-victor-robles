# Imprimiendo mediante indice (siempre comienza desde 0)
peliculas = ["Spiderman", "Batman", "Superman", "Acuaman"]
print(f"{peliculas[0]} es mejor que {peliculas[2]}")

# Imprimiendo valores mediante negativos
print(f"{peliculas[-1]} es mejor que {peliculas[-2]}")

# Imprimiendo un rango de valores de una lista
print(peliculas[1:2])

# Imprimiendo a partir de un rango a un rango no definido
print(peliculas[1:])

# Modificar un indice
pelicula = "Otra cosa"
peliculas[1] = pelicula
peliculas[2] = "El hobbit"
print(peliculas)
