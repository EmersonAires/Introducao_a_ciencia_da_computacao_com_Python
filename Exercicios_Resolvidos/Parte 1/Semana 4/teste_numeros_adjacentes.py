#Fazer um programa para dizer se um determinado número
#possui algarismo adjacentes iguais

numero_entrada= input("Digite um número:")

qtd_algarismo = int(len(numero_entrada))
print(qtd_algarismo)

numero_entrada = int(numero_entrada)

i = 0
qtd_pares = 0

while i < qtd_algarismo:

    numero_temp = numero_entrada // (10**i)
    numero_1 = numero_temp % 10
    numero_aux1 = numero_temp // 10
    numero_2 = numero_aux1 % 10
    if numero_1 == numero_2:
        qtd_pares = qtd_pares + 1
    i = i + 1  
print("A quantidade de duplas adjacentes iguais encontradas é:",qtd_pares)