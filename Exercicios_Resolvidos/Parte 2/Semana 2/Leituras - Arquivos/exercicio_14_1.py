def numero_harmonico():
    ''' Dado um número n inteiro e n > 0, calcula o número harmônico Hn --> Hn = 1 + (1/2) + (1/3) + (1/4) + ... + (1/n) '''


    n = int(input("Digite um número inteiro maior que zero: "))
    
    while n <= 0:
        print("Número digitado <= 0. Digite um número maior que zero!!!")
        n = int(input("Digite um número inteiro maior que zero: "))

    hn = 0
    i = 1

    while i <= n:
        termo = (1/i)
        hn = hn + termo
        print("Termo " + str(i) + " =",termo)
        i += 1
    
    print("Número Harmônico =",hn)

numero_harmonico()


    