def ordenada(lista):
    ''' Receives a list with whole numbers as parameters and returns the boolean True if the list is ordered and False if the list is not ordered'''

    end = (len(lista)-1)

    for i in range(end):
        if lista[i] > lista[i+1]:
            return False
    return True
