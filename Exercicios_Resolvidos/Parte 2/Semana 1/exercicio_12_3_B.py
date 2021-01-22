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

   
    return qtd_bombas


def main(a_mat):
    ''' Imprimi a quantidade de bombas ao redor de cada posição livre '''


    lin_a_mat = 0

    for linha in a_mat:
        col_a_mat = 0

        for elemento in linha:
            if elemento == LIVRE:

                qtd_bombas = conta_bomba(a_mat, lin_a_mat, col_a_mat)
                print("A quantidade de bombas ao redor ao redor da posição livre (" + str(lin_a_mat) + " , " + str(col_a_mat) + ") é igual a: " + str(qtd_bombas) + "bomba(s)")

            col_a_mat +=1
        
        lin_a_mat +=1 



BOMBA = -1
LIVRE = 0

matriz = [[LIVRE, BOMBA, LIVRE, BOMBA], [BOMBA, BOMBA, BOMBA, BOMBA], [LIVRE, LIVRE, BOMBA, LIVRE]]

main(matriz)