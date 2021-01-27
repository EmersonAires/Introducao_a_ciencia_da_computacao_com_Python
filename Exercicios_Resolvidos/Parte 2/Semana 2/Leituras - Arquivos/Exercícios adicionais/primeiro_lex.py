def primeiro_lex(lista):
    ''' Receive a list of the words and returns the firt one in lexgraphic order '''
   
    firt_string = lista[0]

   
    for string in lista:
        str_loop = string
        if str_loop < firt_string:
            firt_string = str_loop
    
    return firt_string
    

def teste():

    lista1 = ["E", "B", "c", "A"]
    lista2 = ["ana", "Ane", "ancelmo", "adriana"]
    lista3 = ["Banana", "morango", "abacaxi", "Acerola"]

    if primeiro_lex(lista1) == "A":
        print("A função primeiro_lex está funcionando corretamente")
    else:
        print("A função primeiro_lex não está funcionando corretamente")
    
    if primeiro_lex(lista2) == "Ane":
        print("A função primeiro_lex está funcionando corretamente")
    else:
        print("A função primeiro_lex não está funcionando corretamente")

    if primeiro_lex(lista3) == "Acerola":
        print("A função primeiro_lex está funcionando corretamente")
    else:
        print("A função primeiro_lex não está funcionando corretamente")


teste()

    