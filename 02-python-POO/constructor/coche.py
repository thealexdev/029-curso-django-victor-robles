class Coche:
    # Propiedades / atributos
    color: "Azul"
    marca: "Nizan"
    modelo: "2026"
    velocidad: 300
    plazas: 2

    # atributos privados
    __soy_privado = "Soy un atributo privado"

    # constructor
    def __init__(self, color, marca, modelo, velocidad, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.plazas = plazas

    # Metodos
    def getPrivado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setVelocidad(self, velocidad):
        self.velocidad = self.velocidad

    def getVelocidad(self):
        return self.velocidad

    def setPlazas(self, plazas):
        self.plazas = plazas

    def getPlazas(self):
        return self.plazas

    def getInfo(self):
        info = "\n ---- Información del coche ----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        info += "\n Plazas: " + str(self.getPlazas())

        return info
