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

        try:
            email = input("Correo: ")
            password = input("Contraseña: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido")
                self.proximasAcciones(login)

        except Exception as error:
            print(type(error))
            print(type(error).__name__)
            print(f"Login incorrecto, intentalo mas tarde")

    def proximasAcciones(self, usuario):

        print("""
            Acciones disponibles:
             - Crear una nota
             - Mostrar notas
             - Eliminar una nota
             - Salir (salir)
        """)

        accion = input("Que quieres hacer?: ")

        if accion == "crear":
            print("Vamor a crear")
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            print("Vamos a mostrar")
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("Vamor a eliminar")
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Hasta pronto {usuario[1]}")
            exit()
