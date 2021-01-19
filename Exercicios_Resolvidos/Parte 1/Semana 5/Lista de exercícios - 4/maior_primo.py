def maior_primo(n):
    if n >= 2:
        k = 2
        while k <= n:
            if éPrimo(k) == "true":
                ultimoprimo = k
                k = k +1
            else:
                k = k + 1
        return ultimoprimo
    
    
   
    
    

def éPrimo(k):
    i = 1
    divisor = 0

    while i <= k:
        if (k % i) == 0:
            divisor = divisor + 1
        i = i + 1

    if divisor == 2 and k > 1:
        return "true"
    else:
        return "false"
        
