def fatorial(numero_entrada):

    n = numero_entrada

    fatorial = 1

    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    
    return fatorial