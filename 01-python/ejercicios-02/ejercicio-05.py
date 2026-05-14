"""

Ejercicio #5

Crear una lista con el contenido de esta tabla

ACCION AVENTURA DEPORTES
GTA     ASSINS  FIFA
COD     CRASH   PRO 21
PUBG    POP     MOTO GP 21

Mostrar esta informacion ordenada

"""

juegos = [
    {"Nombre": "GTA", "Tipo": "Accion"},
    {"Nombre": "COD", "Tipo": "Accion"},
    {"Nombre": "PUBG", "Tipo": "Accion"},
    {"Nombre": "Assins", "Tipo": "Aventura"},
    {"Nombre": "Crash", "Tipo": "Aventura"},
    {"Nombre": "POP", "Tipo": "Aventura"},
    {"Nombre": "Fifa", "Tipo": "Deportes"},
    {"Nombre": "Pro 21", "Tipo": "Deportes"},
    {"Nombre": "Moto GP 21", "Tipo": "Deportes"},
]

print("---   Tipo   ---------   Nombre del Juego   -----")
for juego in juegos:
    print(f"{juego["Tipo"]} ---------------- {juego["Nombre"]}")
