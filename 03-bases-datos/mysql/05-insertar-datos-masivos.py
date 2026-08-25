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

# ver tablas existentes
cursor.execute("SHOW TABLES")
print("----Tablas----")
for table in cursor:
    print(table)

# insertar datos en una tabla de forma masiva
coches = [
    ("seat", "ibiza", 500),
    ("renault", "patito", 5),
    ("chevrolet", "pirata", 20),
    ("mazda", "vendehumo", 600),
]

cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

# hacer commit para ejecutar
database.commit()

# comprobar que se ingresaron los datos en la tabla
# Ejecuta una consulta SELECT para obtener todos los registros de la tabla vehiculos
cursor.execute("SELECT * FROM vehiculos")

# fetchall() recupera todas las filas del resultado de la consulta y las devuelve como una lista de tuplas
resultados = cursor.fetchall()

print("----Datos en la tabla vehiculos----")
for fila in resultados:
    print(fila)
