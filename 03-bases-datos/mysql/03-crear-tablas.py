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

# mostrar las bases de datos creadas
cursor.execute("SHOW DATABASES;")

# imprimir el array
for bd in cursor:
    print(bd)

# crear tablas
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
"""
)

# ver tablas creadas
cursor.execute("SHOW TABLES")
print("----Tablas----")
for table in cursor:
    print(table)
