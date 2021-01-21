
def conta_bomba(a_mat, lin, col):
    ''' Conta a quantidade de bombas ao redor de uma posição (lin, col) de uma matriz '''


    limite_superior = 0
    limite_inferior = (len(a_mat) - 1)
    limite_direito = (len(a_mat[0]) - 1)
    limite_esquerdo = 0
    qtd_bombas = 0
    bomba = -1

    if (lin - 1) >= limite_superior:
        if a_mat[(lin-1)][col] == bomba :
            qtd_bombas = qtd_bombas + 1

    if (lin + 1) <= limite_inferior:
        if a_mat[(lin + 1)][col] == bomba :
            qtd_bombas = qtd_bombas + 1

    if (col - 1) >= limite_esquerdo:
        if a_mat[lin][col - 1] == bomba :
            qtd_bombas = qtd_bombas + 1
    
    if (col + 1) <= limite_direito:
        if a_mat[lin][col + 1] == bomba :
            qtd_bombas = qtd_bombas + 1

    print("A quantidade de bombas encontradas ao redor da posição (" + 
    str(lin) + " , " + str(col) + ") foram : " + str(qtd_bombas))

    return qtd_bombas
    


def teste():
    ''' testa a função conta_bomba '''


    a_mat = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1]]
    lin = 1
    col = 1


    if conta_bomba(a_mat, lin, col) == 2:
        print("Teste 1: função conta_bomba está funcionando corretamente")
    else:
        print("Teste 1: função conta_bomba não está funcionando corretamente")

    lin = 0
    col = 0

    if conta_bomba(a_mat, lin, col) == 1:
        print("Teste 2: função conta_bomba está funcionando corretamente")
    else:
        print("Teste 2: função conta_bomba não está funcionando corretamente")
    
    lin = 2
    col = 2

    if conta_bomba(a_mat, lin, col) == 1:
        print("Teste 3: função conta_bomba está funcionando corretamente")
    else:
        print("Teste 3: função conta_bomba não está funcionando corretamente")

teste()
