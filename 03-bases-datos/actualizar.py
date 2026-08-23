# importando modulo sqlite
import sqlite3

# conexion con la base de datos
conexion = sqlite3.connect("pruebas.db")

# creacion de cursor
cursor = conexion.cursor()

# listar datos de la base de datos con condiciones
cursor.execute(
    """

UPDATE productos SET precio = 811 WHERE precio = 899 ;

"""
)

# guardar cambios
conexion.commit()

# imprimir el resultado
productos = cursor.fetchall()
for producto in productos:
    print(producto)


# cerrar conexion con la base de datos
conexion.close()
