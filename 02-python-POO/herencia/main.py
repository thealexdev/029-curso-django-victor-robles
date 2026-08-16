# Documentación del código: Uso de la clase Persona

"""
Este script demuestra el uso básico de una clase Persona importada desde
un módulo externo llamado 'clases'.
Muestra cómo crear una instancia, establecer sus atributos mediante
métodos setters y acceder a sus propiedades y métodos.
"""

import clases  # Importa el módulo 'clases' que contiene la definición de la clase Persona

# ============================================
# 1. CREACIÓN DE UNA INSTANCIA DE LA CLASE
# ============================================
# Se crea un objeto de tipo Persona utilizando el constructor por defecto
# La sintaxis 'clases.Persona()' accede a la clase Persona dentro del módulo 'clases'
persona = clases.Persona()

# ============================================
# 2. CONFIGURACIÓN DE ATRIBUTOS (SETTERS)
# ============================================
# Se utilizan los métodos setter para asignar valores a los atributos privados
# de la instancia 'persona'

# Establece el nombre de la persona
persona.setNombre("Alejandro")

# Establece los apellidos de la persona
persona.setApellidos("Hernandez")

# Establece la altura de la persona (nota: se usa cadena "19.5", posiblemente en cm o pulgadas)
persona.setAltura("19.5")

# Establece la edad de la persona (nota: se usa cadena "800 Años", valor ficticio/exagerado)
persona.setEdad("800 Años")

# ============================================
# 3. ACCESO A ATRIBUTOS (GETTERS)
# ============================================
# Se accede directamente a los atributos públicos (nombre, apellidos, altura, edad)
# Nota: En una implementación típica, estos atributos podrían ser propiedades
# que devuelven los valores establecidos por los setters

# Muestra el nombre completo de la persona
# Los atributos 'nombre' y 'apellidos' se acceden directamente
print(f"La persona es: {persona.nombre} {persona.apellidos}")

# Muestra la altura almacenada
print(f"Tiene una altura de: {persona.altura}")

# Muestra la edad almacenada
print(f"La persona tiene una edad de: {persona.edad}")

# ============================================
# 4. EJECUCIÓN DE MÉTODOS DE INSTANCIA
# ============================================
# Se invoca el método 'hablar()' que probablemente devuelve un mensaje
# o realiza una acción relacionada con la persona
print(persona.hablar())

# Creamos una instancia de la clase informatico
informatico_01 = clases.Informatico()

# Le asignamos un nombre "Usando el mismo metodo de la clase Persona"
informatico_01.setNombre("Alejandro")

# Imprimos el valor del nombre
print(f"El nombre del informatico es: {informatico_01.nombre}")
print(f"Los lenguajes que sabe este informatico son: {informatico_01.lenguajes}")


tecnico_01 = clases.TecnicoRedes()
tecnico_01.setNombre("Manolin")
print(f"La experiencia del tecnico es de: {tecnico_01.experienciaRedes} años")
print(f"El nombre del informatico es: {tecnico_01.nombre}")

# mostrando la herencia que se obtuvo gracias a super()
print(tecnico_01.lenguajes)
