# Excepciones personalizadas

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Ingresa tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al master en python {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error", e)
