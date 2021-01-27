def fatorial(numero_entrada):

    n = numero_entrada

    fatorial = 1

    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    
    return fatorial



def aproximacao_numerica(e, x):
    ''' calculates an approximation to e raised x '''

    
    term = 0
    i = 0
    less_than_e = False

    while not less_than_e:

        term = ((x**i)/fatorial(i))
        exponential = exponential + term
        i += 1
        if abs(term) < e :
            less_than_e = True

    
