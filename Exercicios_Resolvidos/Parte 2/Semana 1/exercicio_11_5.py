def cria_matriz():
    m = int(input("Digite um número inteiro: "))
    n = int(input("Digite um número inteiro: "))
    matriz = []

    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(int(input("Digite o elemento (" + str(i) + "," + str(j) + ") : ")))
        matriz.append(linha)

    linhas_nulas = 0
    colunas_nulas = 0

    for linha in matriz:
        soma_linha = 0
        for elemento in linha:
            soma_linha = soma_linha + elemento
        if soma_linha == 0:
            linhas_nulas = linhas_nulas + 1
    
    for j in range(n):
        soma_coluna = 0
        for i in range(m):
            soma_coluna = soma_coluna + matriz[i][j]
        if soma_coluna ==0:
            colunas_nulas = colunas_nulas + 1

    
    print("Linhas nulas: ", linhas_nulas)
    print("Colunas nulas: ", colunas_nulas)

cria_matriz()