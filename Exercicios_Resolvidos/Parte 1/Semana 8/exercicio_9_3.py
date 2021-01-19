def remover_repeticao(lista):
    for i in lista:
        k = 1
        while k <= (lista.count(i)-1):
            lista.remove(i)
            k = k + 1          
    lista.sort()  
    return lista  


def lista_dupla():
    n = int(input("digite um número inteiro para a sequência 1: "))
    lista_1 = []
    while n != 0:
        lista_1.append(n)
        n = int(input("digite um número inteiro para a sequência 1: "))   
    
    m = int(input("digite um número inteiro para a sequência 2: "))
    lista_2 = []
    while m != 0:
        lista_2.append(m)
        m = int(input("digite um número inteiro para a sequência 2: "))

    lista_1_2 = []
    lista_1_2 = lista_1 + lista_2

    lista_final = remover_repeticao(lista_1_2)

    print(lista_final)
    

lista_dupla()