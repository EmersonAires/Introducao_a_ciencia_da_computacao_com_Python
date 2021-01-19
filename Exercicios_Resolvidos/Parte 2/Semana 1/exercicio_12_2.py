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
    
    acha_max(matriz)


def acha_max(a_mat):

    max = a_mat[0][0]
    p_linha = 0

    for linha in a_mat:
        p_coluna = 0

        for elemento in linha:
            if max < elemento:
                max = elemento
                max_coluna = p_coluna
                max_linha = p_linha
            
            p_coluna = p_coluna + 1
        
        p_linha = p_linha + 1


    print("O número máximo é:", max, "posicionado na linha: " + str(max_linha) + " e coluna: " + str(max_coluna))

leia_matriz()