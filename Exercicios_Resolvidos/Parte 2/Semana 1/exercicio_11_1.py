def leia_matriz():


    n_linha = int(input("Entre com o número de linhas da matriz: "))
    n_coluna = int(input("Entre com o número de colunas da matriz: "))
    
    matriz = []
    
    for i in range(n_linha):
        linha = []
        for j in range(n_coluna):
            linha.append(int(input("Digite o elemento (" + str(i) + "," + str(j) + "): ")))

        matriz.append(linha)



    print(matriz)     

leia_matriz()