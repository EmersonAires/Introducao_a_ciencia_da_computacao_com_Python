numero_entrada = int(input("Digite o valor de n:"))
n = numero_entrada

fatorial = 1

while n > 0:
    fatorial = fatorial * n
    n = n - 1
    
print(fatorial)