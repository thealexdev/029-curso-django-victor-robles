"""
Bucle While

Estructura de contro que itera o repite la ejecucion de una
serie de intrucciones tantas veces como sea necesario hasta que
deje de cumplirse la condicion

while condicion:
    bloque de instrucciones
    actualizacion de contador
"""

contador = 0

while contador <= 99:
    contador = contador + 1
    print(contador)


"""
Ejemplo con una concatenacion formateada
"""
contador2 = 0
formato = str(0)

while contador2 <= 100:
    formato = formato + "," + str(contador2)
    contador2 = contador2 + 1

print(formato)
