"""
FUNCIONES ANONIMAS
- Son funciones pequeñas que:
- No tienen nombre (de ahí "anónimas")
- Se escriben en una sola línea
- Se usan para tareas simples y repetitivas
"""

dime_el_year = lambda year: f"El año es {year}"

"""
Desglose:

lambda → palabra clave que crea la función anónima
year → parámetro (entrada)
: → separa los parámetros del cuerpo
f"El año es {year}" → lo que devuelve (sin necesidad de return)
"""

print(dime_el_year(2034))
