def entrada_usuario():
    n = int(input("Digite um número inteiro"))
    while n != 0:
        x = fatorial(n)
        print (x)
        n = int(input("Digite um número inteiro"))

def fatorial(n):
    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1
    return fat

