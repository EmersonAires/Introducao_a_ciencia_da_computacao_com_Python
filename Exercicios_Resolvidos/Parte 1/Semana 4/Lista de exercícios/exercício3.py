numero_entrada = input("Digite um número inteiro:")
qtd_algarismo = len(numero_entrada)
numero_entrada = int(numero_entrada)
i = 0
soma_algarismo = 0

while i <= qtd_algarismo:
    numero_auxiliar = numero_entrada // (10**i)
    soma_algarismo = soma_algarismo + (numero_auxiliar % 10)
    i = i +1
    
print(soma_algarismo)