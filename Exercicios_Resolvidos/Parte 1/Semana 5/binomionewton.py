def binomioNewton(n,k):
    if n > k:

        j = n

        fatorial1 = 1

        while j > 0:
            fatorial1 = fatorial1 * j
            j = j - 1
       
        m = k

        fatorial2 = 1

        while m > 0:
            fatorial2 = fatorial2 * m
            m = m - 1
            
        o = (n-k)

        fatorial3 = 1

        while o > 0:
            fatorial3 = fatorial3 * o
            o = o - 1
            
        return (fatorial1/(fatorial2*fatorial3))
    else:
        print("Erro. n tem que ser maior que k. Digite outro valor")