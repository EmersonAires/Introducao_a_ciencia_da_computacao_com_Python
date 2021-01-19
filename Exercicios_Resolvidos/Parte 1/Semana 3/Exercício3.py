NumeroEntrada = int(input("Digite um número inteiro: "))

RestoDivisao = NumeroEntrada % 5

if RestoDivisao == 0:
	print("Buzz")
else:
    print(NumeroEntrada)