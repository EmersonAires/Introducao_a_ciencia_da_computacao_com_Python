def binarySearch(list, item):
    """ Verifica se um item está em um lista ordenada """


    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return found


list = [0, 1, 2, 3 , 4, 5, 6, 7, 8, 9]

binarySearch(list, 3)
