def lista_repeticao(lista):

    lista_final = []
    for i in lista:
        if i not in lista_final:
            lista_final.append(i)
            
    lista_final.sort()
    
    return lista_final


def lista_usuario():
    n = int(input("Digite um número inteiro: "))
    lista = []
    while n != 0:
        lista.append(n)
        n = int(input("Digite um número inteiro: "))
        
    print (lista_repeticao(lista))

lista_usuario()    
