def remove_repetidos(lista):

    lista_final = []
    for i in lista:
        if i not in lista_final:
            lista_final.append(i)
            
    lista_final.sort()
    
    return lista_final


