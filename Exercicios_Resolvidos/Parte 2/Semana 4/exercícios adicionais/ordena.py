def ordena(lista):

    end = len(lista) - 1

    for i in range(end):
        posiçao_menor_elemento = i

        for elemento in lista[(i+1):]:
            if elemento < lista[i]:
                posiçao_menor_elemento = lista.index(elemento)
                lista[i], lista[posiçao_menor_elemento] = lista[posiçao_menor_elemento], lista[i]
    
    return lista