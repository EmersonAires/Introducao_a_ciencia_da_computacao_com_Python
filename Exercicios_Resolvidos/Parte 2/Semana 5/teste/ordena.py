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
