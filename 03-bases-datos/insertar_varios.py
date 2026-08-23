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

productosInsertar = [
    ("Ordenador Portatil", "Laptop 15 pulgadas, 16GB RAM", 899),
    ("Teclado Mecanico", "Switches Cherry MX Red, RGB", 79),
    ("Raton Inalambrico", "Sensor optico 16000 DPI", 45),
    ("Monitor 27 pulgadas", "Resolucion 2K, 144Hz", 329),
    ("Auriculares Gaming", "Sonido envolvente 7.1", 59),
    ("Webcam Full HD", "1080p con microfono integrado", 39),
    ("Disco SSD 1TB", "NVMe M.2, lectura 3500MB/s", 89),
    ("Silla Ergonomica", "Soporte lumbar ajustable", 199),
    ("Impresora Multifuncion", "WiFi, escaner y copiadora", 129),
    ("Router WiFi 6", "Doble banda, alta velocidad", 119),
]
cursor.executemany(
    """

INSERT INTO productos VALUES (?, null,?,?)

""",
    productosInsertar,
)

# guardar cambios
conexion.commit()


# cerrar conexion con la base de datos
conexion.close()
