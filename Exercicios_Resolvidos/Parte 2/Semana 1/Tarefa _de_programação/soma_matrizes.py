def le_matrizes(m1, m2):


    linhas_a_mat = len(m1)
    linhas_b_mat = len(m2)

    matrizes_correspondentes = True

    if linhas_a_mat == linhas_b_mat:
        for i in range(linhas_a_mat):
            if len(m1[i]) != len(m2[i]):
                matrizes_correspondentes = False
    else:
        matrizes_correspondentes = False
    
    return matrizes_correspondentes

def soma_matrizes(m1, m2):


    soma_matrizes = []
    linha_matrizes = []

    if le_matrizes(m1, m2):

        for i in range(len(m1)):
            linha_matrizes = []

            for j in range(len(m1[0])):
                linha_matrizes.append((m1[i][j]+m2[i][j]))
            
            soma_matrizes.append(linha_matrizes)
        
        return soma_matrizes
    
    else:
        return False



m1 = [1]
m2 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

soma_matrizes(m1, m2)
