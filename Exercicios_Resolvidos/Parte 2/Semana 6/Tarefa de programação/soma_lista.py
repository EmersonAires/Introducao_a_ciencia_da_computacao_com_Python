def soma_lista(lista):
    

    if len(lista) == 1:
        return lista[0]
    else:
        somaLista = 0
        for i in range(len(lista)):
            somaLista += soma_lista([lista[i]])
    
    return somaLista
