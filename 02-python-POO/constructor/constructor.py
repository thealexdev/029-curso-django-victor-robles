from coche import Coche

# class Coche(
#  color: Any,
#  marca: Any,
#  modelo: Any,
#  velocidad: Any,
#  plazas: Any
# )
carro01 = Coche("Rojo", "Nissan", "2026", 300, 5)

carro02 = Coche("Azul", "Toyota", "2025", 250, 5)
carro03 = Coche("Negro", "Ford", "2024", 280, 4)
carro04 = Coche("Blanco", "Honda", "2026", 260, 5)
carro05 = Coche("Gris", "Chevrolet", "2023", 240, 7)

print({carro01.getInfo()})
print({carro03.getInfo()})
print({carro02.getInfo()})
print({carro04.getInfo()})
print({carro05.getInfo()})

print({carro01.getPrivado()})


if type(carro01) == Coche:
    print("Es un objeto de tipo Coche")
else:
    print("No es un objeto")
