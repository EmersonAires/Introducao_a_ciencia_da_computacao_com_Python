
def fizzbuzz(n):

    if divisibilidade_3(n) == "true" and divisibilidade_5(n)!= "true":
        return "Fizz"

    if divisibilidade_5(n) == "true" and divisibilidade_3(n)!= "true":
        return "Buzz"
        
    if divisibilidade_5(n) == "true" and divisibilidade_3(n) == "true":
        return "FizzBuzz"
        
    if divisibilidade_5(n) != "true" and divisibilidade_3(n)!= "true":
        return n


def divisibilidade_3(n):

    numero_entrada = str(n)
    qtd_algarismo = len(numero_entrada)
    numero_entrada = int(numero_entrada)
    i = 0
    soma_algarismo = 0

    while i <= qtd_algarismo:
        numero_auxiliar = numero_entrada // (10**i)
        soma_algarismo = soma_algarismo + (numero_auxiliar % 10)
        i = i +1
        
    if soma_algarismo % 3 == 0:
        return "true"


def divisibilidade_5(n):

    if n % 10 == 0 or n % 10 == 5:
        return "true"