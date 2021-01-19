def maior_elemento(lista):
    elemento_ref = lista[0]
    maior_elemento = 0
    for i in lista:
        if i >= elemento_ref:
            maior_elemento = i

    return maior_elemento