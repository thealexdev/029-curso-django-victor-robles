# Programa que valida si una persona tiene la edad minima con 18 años
# para que pueda trabajar o si tiene 65 años como edad maxima parta que
# pueda trabajar usando el operador logico de AND

# edad_minima = 18
# edad_maxima = 65

# edad_usuario = int(input("Ingresa tu edad: "))

# if edad_usuario < edad_minima:
#     print("No puedes trabajar")
# elif edad_usuario > edad_maxima:
#     print("Eres demasiado mayor, no puedes entrar a trabajar")
# else:
#     print("Puedes entrar a trabajar")

edad_minima = 18
edad_maxima = 65

edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= edad_minima and edad_usuario <= edad_maxima:
    print("Puedes entrar a trabajar.")
else:
    print("No puedes trabajar, no tienes la edad apta.")
