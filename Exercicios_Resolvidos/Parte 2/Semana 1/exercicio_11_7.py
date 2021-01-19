def leia_matriz():


    n_linha = int(input("Entre com o número de linhas da matriz: "))
    n_coluna = int(input("Entre com o número de colunas da matriz: "))
    
    matriz = []
    
    for i in range(n_linha):
        linha = []
        for j in range(n_coluna):
            linha.append(int(input("Digite o elemento (" + str(i) + "," + str(j) + "): ")))

        matriz.append(linha)

    return matriz


def inverter_matriz(matriz):


    n_colunas = len(matriz[0])
    n_linhas = len(matriz)
    matriz_invertida = []

    for j in range(n_colunas):
        linha = []
        for i in range(n_linhas):
            linha.append(matriz[i][j])

        matriz_invertida.append(linha)

    return matriz_invertida


def multiplica_matriz():



    a_mat = leia_matriz()
    b_mat = leia_matriz()

    n_colunas_a = len(a_mat[0])
    n_linhas_b = len(b_mat)
    b_mat_invertida = inverter_matriz(b_mat)
    matriz_resultado = []

    for linha_a in a_mat:
        linha_resultado = []

        for linha_invert in b_mat_invertida:
            elemento = 0

            for i in range(n_colunas_a):
                elemento = elemento + (linha_a[i]*linha_invert[i])
            linha_resultado.append(elemento)

        matriz_resultado.append(linha_resultado)

    print(matriz_resultado)



multiplica_matriz()