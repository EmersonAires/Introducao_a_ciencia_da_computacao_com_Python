def soma_hipotenusas(n):
    k = 1
    soma_hipotenusas = 0
    while k <= n:
        i = 1
        while i <= n:
            j = 1
            hipotenusa = 0
            while j <= n:
                hipotenusa = ((i**2) + (j**2))**(1/2)
                if hipotenusa == k:
                    soma_hipotenusas = soma_hipotenusas + k
                    j = n
                    i = n
                j = j + 1
            i = i + 1
        k = k + 1
    return soma_hipotenusas
               
        










   
