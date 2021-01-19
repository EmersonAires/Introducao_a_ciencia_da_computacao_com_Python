def le_matriz(matriz):
    qtd_linhas = len(matriz)
    matriz_quadrada = True

    for linha in matriz:
        if len(linha) != qtd_linhas:
            matriz_quadrada = False
    
    return matriz_quadrada

def cria_matriz():
    n_linhas = int(input("Digite a quantidade de linhas da matriz: "))
    n_colunas = int(input("Digite a quantidade de colunas da matriz: "))
    valor = int(input("Digite o valor de preenchimento da matriz: "))
    matriz = []

    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
    
    if le_matriz(matriz):
        print("matriz quadrada")
    else:
        print("matriz não quadrada")

cria_matriz()

