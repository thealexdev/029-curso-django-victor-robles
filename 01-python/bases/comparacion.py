"""
# Operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""

year = int(input("En que año estamos?: "))

if year == 2021:
    print("Estamos en el año 2021")
elif year > 2021:
    print("Estamos un año adelante del 2021")
else:
    print("Estamos un año anterior al 2021")
