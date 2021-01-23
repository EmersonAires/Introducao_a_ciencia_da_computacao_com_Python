def sao_multiplicaveis(m1, m2):
    ''' Retorna se o número de colunas da matriz a é igual o número de linhas
    da matriz b '''

    n_colunas_a_mat = len(m1[0])
    n_linhas_b_mat = len(m2)

    if n_colunas_a_mat == n_linhas_b_mat:
        matrizes_correspondentes = True
    else:
        matrizes_correspondentes = False
    
    print(matrizes_correspondentes)
    return matrizes_correspondentes

#m1 = [[1, 2, 3], [4, 5, 6]]
#m2 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

#sao_multiplicaveis(m1, m2)