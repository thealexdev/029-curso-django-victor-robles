import usuarios.usuario as modelo


class Acciones:
    def registro(self):
        print("Llena los siguientes campos: ")
        nombre = input("Ingresa tu nombre: ")
        apellidos = input("Ingresa tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)

        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"Perfecto {registro[1].nombre}, te has registrado con el email: {registro[1].email}"
            )
        else:
            print(f"No te has registrado correctamente")

    def login(self):
        print("Introduce tus claves")
        email = input("Correo: ")
        password = input("Contraseña: ")
