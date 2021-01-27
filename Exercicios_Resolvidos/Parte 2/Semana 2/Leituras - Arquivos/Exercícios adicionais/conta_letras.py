def conta_letras(frase, contar="vogais"):
    ''' Account the amount of consonants or vowels that the sentence has'''


    lista_ord_vogais = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    lista_ord_cosoantes = [66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 80,
    81, 82, 83, 84, 86, 87, 88, 89, 90, 98, 99, 100, 102, 103, 104, 106, 107,
    108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122]

    count = 0
    if contar == "vogais":

        for letra in frase:
            for ord_number in lista_ord_vogais:
                if ord(letra) == ord_number:
                    count = count + 1

    else:
        for letra in frase:
            for ord_number in lista_ord_cosoantes:
                if ord(letra) == ord_number:
                    count = count + 1
    
    return count

conta_letras("programamos em python", 'consoantes')