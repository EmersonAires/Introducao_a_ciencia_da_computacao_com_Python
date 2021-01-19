def teste(matriz):
    for j in range(len(matriz[0])):
        coluna = []
        for i in range(len(matriz)):
            coluna.append(matriz[i][j])
        print("elementos da coluna " + str(j + 1) + ": ", coluna)



teste([[1,2,3],["a","b","c"],[10,20,30],[100,200,300]])

