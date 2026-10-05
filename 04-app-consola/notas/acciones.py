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

    def mostrar(self, usuario):
        print(f"\n{usuario[1]}, aqui tienes tus notas: ")
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for nota in notas:
            print("************************")
            print(f"ID: {nota[0]}")
            print(f"TITULO: {nota[2]}")
            print(f"CONTENIDO: {nota[3]}")
            print("************************")

    def borrar(self, usuario):
        print(f"Okey {usuario[1]}, vamos a borrar notas")

        nota_id = int(input("Introduce el id de la nota que quieres borrar: "))

        nota = modelo.Nota(usuario[0], "", "")

        eliminar = nota.eliminar(nota_id)

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")

        else:
            print("No se ha podido borrar la nota")
