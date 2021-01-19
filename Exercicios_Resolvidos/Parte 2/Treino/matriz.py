def cria_matriz(n_linha, n_coluna):
    matriz = []
    i = 0
    while i < n_linha :
        linha_matriz = []
        j = 0
        while j < n_coluna:
            linha_matriz.append(input("Digite o valor de linha [" + str(i) + "], coluna[" + str(j) + "] : "))
            j += 1
        matriz.append(linha_matriz)
        i += 1
    
    return(matriz)

def main():
    n_linha = int(input("Digite o número de linhas da matriz: "))
    n_coluna = int(input("Digite o número de colunas da matriz: "))

    print(cria_matriz(n_linha, n_coluna))


main()