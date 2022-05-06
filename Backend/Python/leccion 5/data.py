#dada la siguiente tupla
# crear una lista que solo incluya los numeros menores a 5

def tuple_excersice():
    tupla = (13, 1, 8, 3, 2, 5, 8)

    # definimos la lista
    p = []

    # flitramos los elementos menores a 5 de la tupla

    for i in tupla:
        if i < 5:
            p.append(i)



    #imprimimos la lista
    return p