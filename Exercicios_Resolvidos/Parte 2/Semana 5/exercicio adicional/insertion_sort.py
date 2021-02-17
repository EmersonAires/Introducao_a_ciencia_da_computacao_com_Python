def insertion_sort(lista):


        for i in range(1, len(lista)):
            element = lista[i] # Guarda o valor do elemento analisado
            j = i
            while j > 0 and lista[j-1] > element:
                lista[j] = lista[j-1]  # Desloca o número para a direita 
                j -= 1
            lista[j] = element # Inseri o elemento na posição adequada
        
        return lista