def soma_numeros():



    text= input("Digite números reais separados por vírgula: ")
    list_numbers = text.split(",")
    sum_numbers = 0

    for number in list_numbers:
        sum_numbers = sum_numbers + int(number)
    
    print(sum_numbers)
    return sum_numbers

soma_numeros()

    