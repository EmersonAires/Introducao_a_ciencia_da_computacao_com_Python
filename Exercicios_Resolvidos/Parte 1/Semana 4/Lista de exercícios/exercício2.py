numero_entrada = int(input("Digite o valor de n:"))

n = 1
count = 1

while count <= numero_entrada:
    divisao = n % 2
    if divisao > 0:
        count = count + 1
        print(n)
        n = n +1
    else:
        n = n +1