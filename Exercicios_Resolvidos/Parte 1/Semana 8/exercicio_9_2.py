def remover_repeticao(lista):
    for i in lista:
        k = 1
        while k <= (lista.count(i)-1):
            lista.remove(i)
            k = k + 1          
    lista.sort()  
    return lista  


def nova_lista():
    n = int(input("digite um número inteiro: "))
    lista = []
    while n != 0:
        lista.append(n)
        n = int(input("digite um número inteiro: "))   
    return remover_repeticao(lista)

nova_lista()