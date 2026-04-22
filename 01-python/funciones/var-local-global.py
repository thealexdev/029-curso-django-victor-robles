"""
Variables locales: Se definen dentro de la funsion y no se puede usar fuera de ella, solo estan disponibles dentro de la misma funsion.

Variables globales: Son las que se declaran fuera de una funsion y estan disponibles dentro y fuera de ellas
"""

frase = "Soy una variable global"

print(frase)


def holaMundo():
    fraseLocal = "Soy una variable local"

    # Convertimos una variable local a una variable global
    global website
    website = "thealexdev.site"
    return fraseLocal, website


print(holaMundo())

"""
Como se actualiza una variable local que se convirtio en global
"""
website = "Fuera de local"
print(website)
