def buscar_en_lista():
    try:
        mensaje = "No hay mensaje que mostrar"
        lista_numeros = [1, 2, 3, 4]
        numero = int(input("Escribe tu numero: "))
        busqueda = numero in lista_numeros
        if busqueda == True:
        # if busqueda <- Podemos simplificar la comprobración
            mensaje = f'El número "{numero}" se encuentra en la lista'
        else:
            mensaje = f'El número "{numero}" no se encuentra en la lista'

        return mensaje
    except:
    # except ValueError <- Capturamos solo el error esperado
        print("Ingresa un valor valido")
        return mensaje


print(buscar_en_lista())
