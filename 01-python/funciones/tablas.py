def tablasMultiplicar(tabla):
    contador = 0
    for tablas in range(1, 11):
        contador = contador + 1
        print(f"{tabla} X {contador} = {tabla * contador}")


for contador in range(1, 11):
    tablasMultiplicar(contador)
    print("---------")
