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

# cerrar conexion
conexion.close()
