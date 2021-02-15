class ordenacao:


    def bolha(self, list):
        end = len(list) - 1

        for i in range(end):
            for j in range(end):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]  # Troca de posição

        return list


    def bolha_otimizado(self, list):

        end = len(list) - 1

        troca = True
        for i in range(end):

            if troca:
                troca = False
                for j in range(end):
                    if list[j] > list[j+1]:
                        list[j], list[j+1] = list[j+1], list[j]  # Troca de posição
                        troca = True
            else:
                return list

        return list

    def insercao(self, list):


        for i in range(1, len(list)):
            element = list[i] # Guarda o valor do elemento analisado
            j = i
            while j > 0 and list[j-1] > element:
                list[j] = list[j-1]  # Desloca o número para a direita 
                j -= 1
            list[j] = element # Inseri o elemento na posição adequada
        
        return list
    
    def selecao(self, list):


        for i in range(len(list)-1):
            min = i       # considera o prímeiro elemento como mínimo inicial

            for j in range(i+1, len(list)):
                if list[j] < list[min]:
                    min = j             # nova posição do mínimo

            if min != i:
                list[min], list[i] = list[i], list[min] # Inverte as posições
        
        return list

ord = ordenacao()
list = [5, 4, 3, 2, 1]

ord.selecao(list)