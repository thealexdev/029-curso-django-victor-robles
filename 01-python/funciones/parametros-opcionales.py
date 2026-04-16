def nombres(nombre, apellido=None):
    if apellido != None:
        print(f"{nombre} {apellido}")
    else:
        print(nombre)


nombres("Alex")
