nombre = "Alejandro Hernandez"


def mostrarNombre(nombre, edad):
    print(f"Hola {nombre}")

    if edad >= 40:
            print("Eres un adulto mayor")
    elif edad >= 18:
        print("Eres mayor de edad")
    elif edad <= 17:
        print("Eres menor de edad")
    else:
        print("Introduce un numero de edad valido")


nombre = input("Introduce tu nombre: ")
edad = int(input("Dime tu edad: "))
mostrarNombre(nombre, edad)
