def busca(lista, elemento):
    '''Searches for an end element in a list and returns the index
     corresponding to the position of the element found'''
    
    for i in range(len(lista)):

       if lista[i] == elemento:
           return i

    return False 