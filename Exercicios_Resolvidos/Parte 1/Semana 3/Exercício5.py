NumeroEntrada1 = int(input("Digite o prímeiro número inteiro: "))
NumeroEntrada2 = int(input("Digite o segundo número inteiro: "))
NumeroEntrada3 = int(input("Digite o terceiro número inteiro: "))

if NumeroEntrada1 < NumeroEntrada2 and NumeroEntrada2 < NumeroEntrada3 :
	print("crescente")
else:
    print("não está em ordem crescente")