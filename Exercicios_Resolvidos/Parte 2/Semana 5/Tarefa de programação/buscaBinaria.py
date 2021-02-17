def busca(lista, elemento):
    """ Verifica se um item está em um lista ordenada """


    first = 0
    last = len(lista) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lista[midpoint] == elemento:
            found = True
            print(midpoint)
            return midpoint
        else:
            print(midpoint)
            if elemento < lista[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return found
