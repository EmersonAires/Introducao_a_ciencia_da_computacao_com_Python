#Exercício 01
#Verificar se o número é par ou ímpar

NumeroEntrada = int(input("Digite um número inteiro: "))

RestoDivisao = NumeroEntrada % 2

if RestoDivisao == 0:
	print("Par")
else:
    print("Ímpar")