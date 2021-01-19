def partida():
     n = int(input("Quantas peças? "))
     m = int(input("Limite de peças por jogada? "))
     voce_comeca = False
     computador_comeca = False
     if n % (m+1) == 0:
        computador_comeca = True
        print("Computador começa!")
     else:
        voce_comeca = True
        print("Você começa!")
     
     