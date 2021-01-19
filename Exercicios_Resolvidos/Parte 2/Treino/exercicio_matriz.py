def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        linha = []
        for j in range(num_linhas):
            valor = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

cria_matriz(2,3)