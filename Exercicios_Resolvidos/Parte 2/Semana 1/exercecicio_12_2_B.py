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
    
    ordem_decrescente(matriz)


def ordem_decrescente(a_mat):

    matriz_decrescente = []
    linha = 0
    for linha_a_mat in a_mat:
        coluna = 0
        for coluna_a_mat in linha_a_mat:
            matriz_decrescente.append([coluna_a_mat, linha, coluna])
            coluna += 1
        linha +=1
    
    matriz_decrescente.sort()
    matriz_decrescente.reverse()

    for linha in matriz_decrescente:
        print("Elemento:",linha[0],", Linha:", linha[1],", Coluna:", linha[2])
            




   
leia_matriz()