# importando modulo sqlite
import sqlite3

# conexion con la base de datos
conexion = sqlite3.connect("pruebas.db")

# creacion de cursor
cursor = conexion.cursor()

# listar datos de la base de datos
cursor.execute(
"""

SELECT * FROM productos;

"""
)

# imprimir el resultado
productos = cursor.fetchall()
for producto in productos:
    print(producto)

# Borrar registros
cursor.execute(
"""
DELETE FROM productos

""")

# guardar cambios
conexion.commit()


# cerrar conexion con la base de datos
conexion.close()
