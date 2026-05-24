def elevar_cuadrado():
    try:
        numero = int(input("Dime un numero para elevarlo al cuadrado: "))
        mensaje = f"El cuadrado de un numero es: {numero * numero}"
        return mensaje
    # except ValueError:
    #     print("Debes ingresar un numero entero")
    #     return "Corrige los errores"
    # except TypeError:
    #     print("Introduce un numero")
    #     return "Corrige los errores"
    except Exception as error:
        print("Ha ocurrido un error: " + type(error).__name__)
        return "Corrige los errores"


print(elevar_cuadrado())
