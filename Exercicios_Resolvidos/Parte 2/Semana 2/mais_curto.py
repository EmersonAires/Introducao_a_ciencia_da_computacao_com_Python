def mais_curto(lista):

    comp_base = len(lista[0].strip())
    nome_mais_curto = lista[0].strip().capitalize()

    for nome in lista:
        if len(nome.strip()) < comp_base:
            nome_mais_curto = nome.capitalize()

    print(nome_mais_curto)

lista = ["ana", "adrina", "mariano", "di"]

mais_curto(lista)
