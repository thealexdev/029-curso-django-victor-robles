"""
For
for variable in elemento iterable (lista, rango, etc)
    bloque de instrucciones

"""

contador = 0

for contador in range(0, 10):
    print("voy en el numero" + str(contador))

cantidad = 0
suma = 0

# suma mediante for
for cantidad in range(0, 10):
    suma = suma + cantidad

print(f"El resultado final es de: {suma}")
