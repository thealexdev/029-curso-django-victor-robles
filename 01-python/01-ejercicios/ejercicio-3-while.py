numero = 0
multiplicacion = int(input("Ingresa el numero de la tabla: "))

if multiplicacion < 1:
    print("Ingresa un numero valido del 1 al 10")
elif multiplicacion > 10:
    print("Ingresa un numero valido del 1 al 10")
else:
    while numero <= 9:
        numero = numero + 1
        print(f"{multiplicacion} X {numero} = {multiplicacion * numero}")
