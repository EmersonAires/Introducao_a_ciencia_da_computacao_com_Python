def leia_matriz():
    '''Retorna uma matriz inserida pelo usuário'''


    n_linha = int(input("Entre com o número de linhas da matriz: "))
    n_coluna = int(input("Entre com o número de colunas da matriz: "))
    
    matriz = []
    
    for i in range(n_linha):
        linha = []
        for j in range(n_coluna):
            linha.append(int(input("Digite o elemento (" + str(i) + "," + str(j) + "): ")))

        matriz.append(linha)
    
    return matriz

###############################################################################

def verifica_matrizes(a_mat, b_mat):
    ''' Retorna se o número de colunas da matriz a é igual o número de linhas
    da matriz b '''

    n_colunas_a_mat = len(a_mat[0])
    n_linhas_b_mat = len(b_mat)

    if n_colunas_a_mat == n_linhas_b_mat:
        matrizes_correspondentes = True
    else:
        matrizes_correspondentes = False
    
    return matrizes_correspondentes

#################################################################################

def extrair_coluna(b_mat, col):
    '''retorna uma lista com os elementos da coluna indicada'''


    coluna_b_mat = []

    for linha in b_mat:
        elemento = linha[col]
        coluna_b_mat.append(elemento)

    return coluna_b_mat


################################################################################

def teste_lin(b_mat):
    ''' Retorna um valor de linha válido'''

    teste_linha = True
    lin = int(input("Digite o número da linha: "))
    
    while teste_linha:

        if lin < len(b_mat):
            teste_linha = False
        else:
            print("Digite um número de linha válido")
            lin = int(input("Digite o número da linha: "))
    
    return lin

#################################################################################

def teste_col(a_mat):
    ''' Retorna um valor de coluna válido'''

    teste_coluna = True
    col = int(input("Digite o número da coluna: "))

    while teste_coluna:

        if col < len(a_mat[0]):
                teste_coluna = False
        else:
            print("Digite um número de coluna válido")
            col = int(input("Digite o número da coluna: "))
    
    return col
    
#################################################################################

def produto_lincol(lin, a_mat, col, b_mat):
    ''' Retorna a soma do produto de uma linha de uma matriz a_mat
     pela coluna de uma matriz b_mat'''
   
    linha_temp = a_mat[lin]
    coluna_temp = extrair_coluna(b_mat, col)
    soma_produto = 0

    for i in range(len(linha_temp)):

        soma_produto = soma_produto + (linha_temp[i]*coluna_temp[i])
    
    print("O resultado da soma do produto da linha " + str(lin) + " da matriz A pela coluna " + str(col) + " da matriz B é igual a:", soma_produto)

    return soma_produto



#################################################################################

def main():

    a_mat = leia_matriz()
    b_mat = leia_matriz()

    if verifica_matrizes(a_mat, b_mat):
        lin = teste_lin(b_mat)
        col = teste_col(a_mat)
        produto_lincol(lin, a_mat, col, b_mat)

    else:
        print("O número de colunas da Matriz A não é igual ao número de linhas da matriz B")

 
#################################################################################
    
def teste_verifica_matrizes():
    
    a_mat = [[1, 1, 1], [1, 1, 1]]
    b_mat = [[2, 2], [2, 2], [2, 2]]
    c_mat = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]

    if verifica_matrizes(a_mat, b_mat):
        print("A função verifica_matrizes está funcionando")
    else:
        print("A função verifica_matrizes não está funcionando")

#######################################################################################

def teste_extrair_coluna():

    a_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    col_a_mat = extrair_coluna(a_mat, 0)

    if col_a_mat == [1, 4, 7]:
        print("A função extrair_coluna está funcionando")
    else:
        print("A função extrair_coluna não está funcionando")


def teste_teste_lin():



    a_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    if teste_lin(a_mat) < len(a_mat):
        print("A função teste_lin está funcionando")
    else:
        print("A função teste_lin não está funcionando")

    if teste_col(a_mat) < len(a_mat[0]):
        print("A função teste_col está funcionando")
    else:
        print("A função teste_col não está funcionando")




def teste_produto_lincol():

    lin = 0
    col = 0
    a_mat = [[1, 1, 1], [2, 3, 4]]
    b_mat = [[1, 2, 3], [1, 4, 5], [1, 6, 7]]

    if produto_lincol(lin, a_mat, col, b_mat) != 3:
        print ("A função produto_lincol não está funcionado corretamente")
    else:
        print("A função produto_lincol está funcionando corretamente")


main()
