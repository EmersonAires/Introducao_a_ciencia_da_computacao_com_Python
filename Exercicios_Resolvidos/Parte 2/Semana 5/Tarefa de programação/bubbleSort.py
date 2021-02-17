def bubble_sort(lista):
        end = len(lista) - 1

        for i in range(end):
            for j in range(end):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]  # Troca de posição
                    print(lista)
        return lista
