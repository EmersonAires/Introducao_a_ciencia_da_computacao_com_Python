numero_entrada = int(input("Digite um número inteiro: "))
controle= len(str(numero_entrada))
i=0
soma=0

while i < controle:
    parte_inteira = numero_entrada//(10**i)
    parte_decimal = parte_inteira % 10
    soma = soma + parte_decimal
    i = i +1
    
print("A soma dos algarismos do número é:",soma)