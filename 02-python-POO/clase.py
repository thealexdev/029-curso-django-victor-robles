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

    def getVelocidad(self):
        return self.velocidad


# fin de la definicion de la clase

# crear un objeto / instanciar la clase
coche = Coche()
# podemos imprimir el valor de una propiedad de la clase
print(f"La velocidad del coche es: {coche.velocidad}")
# ejecutamos un metodo
coche.acelerar()
print(f"La velocidad del coche es: {coche.velocidad}")
