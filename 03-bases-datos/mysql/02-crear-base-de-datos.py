import mysql.connector

# conexion con la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="master_python",
)

# ¿La conexion ha sido correcta?
print(database)

# creacion del cursor
cursor = database.cursor()

# creacion de una base de datos
cursor.execute("CREATE DATABASE master_python_02")

# mostrar las bases de datos creadas
cursor.execute("SHOW DATABASES;")

# imprimir el array
for bd in cursor:
    print(bd)
