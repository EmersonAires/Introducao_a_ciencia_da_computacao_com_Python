n = int(input("Digite uma sequência de números: "))
lista = []

while n != 0 :
    lista.append(n)
    n = int(input("Digite uma sequência de números: "))

x = int(len(lista))

k = -1
while k >= -x :
    print(lista[k])
    k = k - 1
    
