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


def multiplica_matriz(a_mat, b_mat):


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







a = [[1, 2, -1], [0, 3, 2]]
b = [[1, -1], [2, 0], [3, 2]]

multiplica_matriz(a, b)