import ordena
import time
import random


def big_list(x=100):
    """ recebe um número inteiro x e devolve uma lista com x elementos """
    lista = [random.randrange(1000) for i in range(x)]

    return lista

def organiza():


    lista = big_list(10000)
    ord = ordena.ordenacao()
    inicio = time.time()
    lista_ord = ord.bolha(lista)
    fim = time.time()

    print("O tempo gasto para executar o algoritimo bolha foi: ", (fim - inicio))
    print("#####################################################################")

    inicio = time.time()
    lista_ord = ord.bolha_otimizado(lista)
    fim = time.time()

    print("O tempo gasto para executar o algoritimo bolha_otimizado foi: ", (fim - inicio))


organiza()