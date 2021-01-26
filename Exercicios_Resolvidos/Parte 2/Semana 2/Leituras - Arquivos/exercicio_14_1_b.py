def numero_harmonico():
    ''' Dado um número n inteiro e n > 0, calcula o número harmônico Hn --> Hn = 1 + (1/2) + (1/3) + (1/4) + ... + (1/n) '''


    n = int(input("Digite um número inteiro maior que zero: "))
    
    while n <= 0:
        print("Número digitado <= 0. Digite um número maior que zero!!!")
        n = int(input("Digite um número inteiro maior que zero: "))

    hn = 0

    while n > 0 :
        termo = (1/n)
        hn = hn + termo
        print("Termo " + str(n) + " =",termo)
        n -= 1
    
    print("Número Harmônico =",hn)

numero_harmonico()


    