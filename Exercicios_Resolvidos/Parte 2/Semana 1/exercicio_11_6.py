def le_matriz(a_mat, b_mat):


    linhas_a_mat = len(a_mat)
    linhas_b_mat = len(b_mat)

    matrizes_correspondentes = True

    if linhas_a_mat == linhas_b_mat:
        for i in range(linhas_a_mat):
            if len(a_mat[i]) != len(b_mat[i]):
                matrizes_correspondentes = False
    
    return matrizes_correspondentes

   



def multiplica_matriz(a_mat, b_mat):



    resultado = []


    if le_matriz(a_mat) and le_matriz(b_mat):
        pass





a_mat = [[1, 2, 3], [4, 5, 6]]

b_mat = [[1, 2, 3], [4, 5, 6]]

#le_matriz(a_mat, b_mat)
