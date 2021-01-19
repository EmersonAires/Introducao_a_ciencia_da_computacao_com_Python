
def n_primos(n):
    i = 0
    k = 0
    qtd_primos = 0
    while i < (n-1):
        k = n - i
        if éPrimo(k) == "True":
            qtd_primos = qtd_primos + 1
            i = i + 1
        else:
            i = i + 1
    return qtd_primos
    

def éPrimo(k):
    i = 1
    divisor = 0

    while i <= k:
        if (k % i) == 0:
            divisor = divisor + 1
        i = i + 1

    if divisor == 2 and k > 1:
        return "True"
    else:
        return "False"
        

