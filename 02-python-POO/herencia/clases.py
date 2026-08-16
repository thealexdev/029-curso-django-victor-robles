# Es la posibilidad de compartir atributos y metodos entre clases


class Persona:
    # nombre
    # apellidos4
    # altura
    # edad

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self0):
        return "Estoy durmiendo"


# hereda de la clase padre
class Informatico(Persona):
    # lenguajes
    # experiencia
    def __init__(self):
        self.lenguajes = "HTML, CSS, JS, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "He reparado tu PC"


class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() # permite ingresar a los atributos y metodos de la clase padre heradada
        self.auditarRedes = "Expoerto"
        self.experienciaRedes = 15

        def auditoria(self):
            return "Estoy auditando"
