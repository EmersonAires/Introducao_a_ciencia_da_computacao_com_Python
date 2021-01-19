def sequencia():
    n = int(input("Digite a quantidade de números da sequência: "))
    seq = []
    count = 0
    while count < n :
        num = int(input("Digite um número inteiro: "))
        seq.append(num)
        count += 1

    seq.reverse()
    print(seq)

sequencia()
