"""
# Crea un programa con ifs anidados que verifique se un estudiante tiene ine, tiene mayoria de edad y puede ingresar:

- Si es estudiante es mayor de edad puede pasar
- Si el estudiante es mayor pero reprobo, no puede pasar
"""

reprobo = False
edad = 18

if edad >= 18:
    if reprobo == True:
        print("El estudiante no puede pasar")
    else:
        print("El estudiante puede pasar")
else:
    print("El estudiante no puede pasar")
