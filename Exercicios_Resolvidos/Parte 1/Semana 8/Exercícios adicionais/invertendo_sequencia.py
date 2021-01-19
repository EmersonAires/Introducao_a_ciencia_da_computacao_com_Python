def invertendo_sequencia():
    n = int(input("Digite um número inteiro: "))
    lista = []
    while n != 0:
        lista.append(n)
        n = int(input("Digite um número inteiro: "))
    
    lista.reverse()

    for i in lista:
        print(i)

invertendo_sequencia()