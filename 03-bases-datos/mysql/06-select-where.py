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

# comprobar que se ingresaron los datos en la tabla
# Ejecuta una consulta SELECT para obtener todos los registros de la tabla vehiculos
cursor.execute("SELECT * FROM vehiculos")

# fetchall() recupera todas las filas del resultado de la consulta y las devuelve como una lista de tuplas
resultados = cursor.fetchall()

print("----Datos en la tabla vehiculos----")
for fila in resultados:
    print(fila)

print("--- imprimir solo un dato de la tabla ---")
for fila in resultados:
    print(fila[1], fila[2])


cursor.execute("SELECT * FROM vehiculos where PRECIO <= 18500 AND marca = 'seat'")
resultados2 = cursor.fetchall() # fetchone <- solo sacara un dato siempre, el primero que se guardo
print("----Datos en la tabla vehiculos con WHERE Y AND----")
for fila in resultados2:
    print(fila)