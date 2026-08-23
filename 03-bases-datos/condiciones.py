# importando modulo sqlite
import sqlite3

# conexion con la base de datos
conexion = sqlite3.connect("pruebas.db")

# creacion de cursor
cursor = conexion.cursor()

# listar datos de la base de datos con condiciones
cursor.execute(
    """

SELECT * FROM productos WHERE precio >= 800;

"""
)

# imprimir el resultado
productos = cursor.fetchall()
for producto in productos:
    print(producto)


# guardar cambios
conexion.commit()


# cerrar conexion con la base de datos
conexion.close()
