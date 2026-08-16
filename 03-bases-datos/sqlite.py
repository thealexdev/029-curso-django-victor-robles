# importar modulo
import sqlite3

# conexion a la base de datos
conexion = sqlite3.connect("pruebas.db")

# crear cursor (permite ejecutar consulta)
cursor = conexion.cursor()

# crear una tabla
cursor.execute(
    "CREATE TABLE IF NOT EXISTS productos(" + "titulo VARCHAR(255), "
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    + "descripcion TEXT, "
    + "precio int(255)"
    + ")",
)

# guardar cambios
conexion.commit()

# # insertar datos
cursor.execute(
    "INSERT INTO productos (titulo, descripcion, precio) VALUES ('primer producto', 'descripcion de mi producto', 550)"
)
# guardar
conexion.commit()

# listar datos
cursor.execute("SELECT * FROM productos;")

# obtener los datos en forma de tupla
productos = cursor.fetchall()

# imprimimos el resultado
for producto in productos:
    print(producto)


# consultar solo el nombre
cursor.execute("SELECT titulo FROM productos;")

# sacar el primer registro
producto = cursor.fetchone()
print(producto)

# cerrar conexion
conexion.close()
