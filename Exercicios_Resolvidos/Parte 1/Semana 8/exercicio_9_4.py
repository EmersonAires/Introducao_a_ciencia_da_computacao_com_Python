def soma_segmentos(lista):
    comp_seg = 1
    comp_seg_max = len(lista)
    soma_atual = 0
    soma_anterior = 0
    lista_temp = []
    segmento_maior_soma = []
    while comp_seg <= comp_seg_max:
        i = 0
        teste_comp = True
        while i <= (comp_seg_max - 1) and teste_comp:
            lista_temp = lista[i:(i+comp_seg)].copy()
            if len(lista_temp) == comp_seg:
                for k in lista_temp:
                    soma_atual = soma_atual + k
                if soma_atual > soma_anterior:
                    soma_anterior = soma_atual
                    segmento_maior_soma = lista_temp.copy()
                soma_atual = 0
            else:
                teste_comp = False
            i = i + 1
        comp_seg = comp_seg + 1
    print("O segmento de sequêcia que possui a maior soma é :",segmento_maior_soma,"cuja soma é :",soma_anterior)

def lista_segmento():
    n = int(input("Digite a quantidade de números da sequência: "))
    i = 1
    lista = []

    while i <= n:
        k = int(input("Digite um número da sequência: "))
        lista.append(k)
        i = i + 1
    print(lista)

    soma_segmentos(lista)
lista_segmento()