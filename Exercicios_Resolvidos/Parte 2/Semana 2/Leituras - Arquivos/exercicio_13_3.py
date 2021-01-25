def read_file():
    ''' Read file and return a list with lines '''


    path = "C:\\Users\emerson eduardo\\Desktop\\Engenharia Civil\\Cursos\\Introdução a ciência da computação com python\\Introdu--o-a-ci-ncia-da-computa--o-com-python\\Exercicios_Resolvidos\\Parte 2\\Semana 2\\Leituras - Arquivos\\numeros.txt"

    list_lines = []

    with open(path, "r", encoding= "utf-8") as file:
        for line in file:
            list_lines.append(line.split())

    print_sum(list_lines)




def print_sum(list_lines):
    ''' Prints the sum of each line and the total '''

    total = 0
    
    for line in list_lines:
        sum_line = 0
        for number in line:
            sum_line = sum_line + int(number)

        total = total + sum_line
        print("Soma =",sum_line)

    print("Total =",total)




read_file()
