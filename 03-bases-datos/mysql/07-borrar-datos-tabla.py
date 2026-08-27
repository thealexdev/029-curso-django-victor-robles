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
cursor = database.cursor(buffered=True)

# ver tablas existentes
cursor.execute("SHOW TABLES")
print("----Tablas----")
for table in cursor:
    print(table)

# eliminar un dato de una tabla
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Opel'")
database.commit()

# comprobar que se ingresaron los datos en la tabla
# Ejecuta una consulta SELECT para obtener todos los registros de la tabla vehiculos
cursor.execute("SELECT * FROM vehiculos")

# fetchall() recupera todas las filas del resultado de la consulta y las devuelve como una lista de tuplas
resultados = cursor.fetchall()

print("----Datos en la tabla vehiculos----")
for fila in resultados:
    print(fila)

# ver que dato se elimino
print(cursor.rowcount, "borrados!!!")
