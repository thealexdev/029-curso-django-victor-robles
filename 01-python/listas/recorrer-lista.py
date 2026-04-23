peliculas = ["Batman", "Batman 2", "Ejemplo"]
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


for pelicula in peliculas:
    print(f"{pelicula} - # {peliculas.index(pelicula)+1}")
