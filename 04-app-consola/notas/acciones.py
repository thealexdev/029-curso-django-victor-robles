import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]}, vamos a crear una nueva nota")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Ingresa el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto haz guardado la nota: {nota.titulo}")

        else:
            print(f"No se ha guardado la nota")
