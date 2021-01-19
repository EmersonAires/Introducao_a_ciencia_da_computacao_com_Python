NumeroEntrada = int(input("Digite um número inteiro: "))

RestoDivisao1 = NumeroEntrada % 3
RestoDivisao2 = NumeroEntrada % 5

if RestoDivisao1 == 0 and RestoDivisao2 == 0:
	print("FizzBuzz")
else:
    print(NumeroEntrada)