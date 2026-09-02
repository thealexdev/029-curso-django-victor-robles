import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="app_consola",
)

print(database)

cursor = database.cursor(buffered=True)


class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        return self.nombre

    def identificar(self):
        return self.nombre
