def main():
    largura = int(input("Digite a largura do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))
    i = 0
    while i < altura:

        if i == 0 or i == (altura-1):
            preencher_completo(largura)
        else:
            preecher_vazado(largura)
        print()
        i = i + 1
    
def preencher_completo(largura):
    j = 0
    while j < largura:
            print("#",end="")
            j = j + 1
            
def preecher_vazado (largura):
    j = 0
    while j < largura:
    
        if j == 0 or j == (largura-1):
            print ("#", end="")
        else:
            print(" ", end="")
        j = j + 1
        
x = main()
