# Clases

# definir una clase (molde para crear mas objetos de ese tipo)
# coche (con caracteristicas similares)


class Coche:
    # atributos / propiedades
    # caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # metodos = acciones/funciones que hace el objeto en cuestion
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def serModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def getVelocidad(self):
        return self.velocidad


# fin de la definicion de la clase

# crear un objeto / instanciar la clase
coche = Coche()
# podemos imprimir el valor de una propiedad de la clase
print(f"La velocidad del coche es: {coche.velocidad}")
# ejecutamos un metodo
coche.acelerar()
print(
    f"La velocidad del coche es: {coche.velocidad}"
)  #! <- Esto es una mala practica, siempre se debe de buscar que sean los metodos los que interactuen con las propiedades, no interactuar con las propiedades directamente

print(
    f"La velocidad del coche es: {coche.getVelocidad()}"
)  # ? Forma correcta de interactuar con las propiedades de la clase

# color del coche
print(f"El color del coche es: {coche.getColor()}")
coche.setColor("Azul")
print(f"El color del coche es: {coche.getColor()}")
