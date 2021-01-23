def imprime_matriz(matriz):
    ''' Imprime uma matriz linha por linha'''

    qtd_elementos = (len(matriz[0]) - 1)


    for linha in matriz:
        i = 0
        for elemento in linha:
            if i < qtd_elementos:
                print(elemento, end =" ")
            else:
                print(elemento, end ="")

            i += 1

        print()



matriz = [[1, 1, 1], [2, 2, 2]]


imprime_matriz(matriz)