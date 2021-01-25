def separa(texto, sep):
    ''' Recebe uma string e a separa de acordo com o caracter separador recebido '''

    lista = texto.split(sep)
    return lista


def maior_palavra():
    
    texto = input("Digite palavras separadas por vírgula: ")
    list_words = separa(texto, ",")
    length_word = 0
    bigger_word = ""

    for word in list_words:
        if len(word) > length_word :
            bigger_word = word
            length_word = len(word)
    
    print(bigger_word)


maior_palavra()