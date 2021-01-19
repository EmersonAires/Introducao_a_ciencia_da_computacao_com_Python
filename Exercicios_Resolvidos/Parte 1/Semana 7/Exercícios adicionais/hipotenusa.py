def soma_hipotenusas(n):
    i = 1
    hipotenusa = 0
    soma_hipotenusas = 0
    while i <= n:
        j = 1
        while j <= n:
            hipotenusa = ((i**2) + (j**2))**(1/2)
            if hipotenusa != 0 and hipotenusa//1 == hipotenusa and hipotenusa <= n:
                soma_hipotenusas = soma_hipotenusas + hipotenusa
            j = j + 1
        i = i + 1
    
    return int(soma_hipotenusas/2)

#def soma_hipotenusas(hipotenusa):
    #soma_hipotenusas = 0
    #soma_hipotenusas = soma_hipotenusas + hipotenusa
    #return soma_hipotenusas
