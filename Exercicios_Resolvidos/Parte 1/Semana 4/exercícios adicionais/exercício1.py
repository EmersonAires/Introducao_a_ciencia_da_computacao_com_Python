numero_entrada = int(input("Digite um número inteiro:"))

i = 1
divisor = 0

while i <= numero_entrada:
    if (numero_entrada % i) == 0:
        divisor = divisor + 1
    i = i + 1

if divisor == 2 and numero_entrada > 1:
    print("primo")
else:
    print("não primo")