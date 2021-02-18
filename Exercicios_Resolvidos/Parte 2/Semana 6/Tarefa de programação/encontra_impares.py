def encontra_impares(lista):

    if len(lista) == 1:
        if lista[0] % 2 != 0:
            return lista
        else:
            return []
    else:
        lista_impares = []
        for i in range(len(lista)):
            if len(encontra_impares([lista[i]])) == 1 :
                lista_impares.extend([lista[i]])
    

    return lista_impares


