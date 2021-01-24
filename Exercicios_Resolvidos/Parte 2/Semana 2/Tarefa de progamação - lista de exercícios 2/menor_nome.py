def menor_nome(nomes):

    comp_base = len(nomes[0].strip())
    nome_mais_curto = nomes[0].strip().capitalize()

    for nome in nomes:
        if len(nome.strip()) < comp_base:
            nome_mais_curto = nome.strip().capitalize()

    return nome_mais_curto

#nomes = ["ana", "adrina", "mariano", "di"]

#menor_nome(nomes)
