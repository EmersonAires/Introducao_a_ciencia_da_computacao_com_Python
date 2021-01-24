def maiusculas(frase):

    comprimento_frase = len(frase)
    i = 0
    frase_resultado = ""
    while i < comprimento_frase:
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            frase_resultado = frase_resultado + frase[i]
        i += 1
    
    return frase_resultado
