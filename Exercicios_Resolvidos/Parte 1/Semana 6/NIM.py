def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1- para jogar uma partida isolada")
    print("2- para jogar um campeonato")
    
    modalidade = input("Escolha a modalidade")
    teste_modalidade = True
    
    while teste_modalidade:
        if modalidade == "1":
            teste_modalidade = False
            print("Você escolheu uma partida isolada!")
            partida()  
        elif modalidade == "2":
            teste_modalidade = False
            print("Você escolheu um campeonato!")
            campeonato()
        else: 
            print("Insira um valor válido")
            modalidade = input("Escolha a modalidade")
            
def computador_escolhe_jogada(n,m):
    teste = m + 1
    i = 1
    proxima_jogada = 0
    while i <= n :
        resto = n - i
        if resto % teste == 0 and (n - resto) <= m and (n - resto) != 0:
            proxima_jogada = (n - resto)
            i = n + 1
        else:
            i = i + 1
    if proxima_jogada == 0:
        if m <= n:
            proxima_jogada = m
        else:
            proxima_jogada = n
        return proxima_jogada
    else:
        return proxima_jogada
 
def usuario_escolhe_jogada(n, m):
    proxima_jogada = int(input("Quantas peças você vai tirar?"))
    jogada_valida = False
    while jogada_valida == False: 
        if proxima_jogada > 0 and proxima_jogada <= m and proxima_jogada <= n:
            jogada_valida = True
        else:
            print ("Oops! Jogada inválida! Tente de novo.")
            proxima_jogada = int(input("Quantas peças você vai tirar?"))     
    return proxima_jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vencedor = 0
    voce_comeca = False
    computador_comeca = False
    if n % (m+1) != 0:
        computador_comeca = True
        print("Computador começa!")
    else:
        voce_comeca = True
        print("Você começa!")
     
    while n > 0 :
        if voce_comeca:
            peças_retiradas = usuario_escolhe_jogada(n, m)
            n = n - peças_retiradas
            print("Você tirou",peças_retiradas,"peça(s)")
            print("Restaram:",n,"peças no tabuleiro")
            voce_comeca = False
            computador_comeca = True
            if n == 0:
                vencedor = 1
                
        else:
            peças_retiradas_comp = computador_escolhe_jogada(n, m)
            n = n - peças_retiradas_comp
            print("O computador tirou",peças_retiradas_comp,"peça(s)")
            print("Restaram:",n,"peças no tabuleiro")
            voce_comeca = True
            computador_comeca = False
            if n == 0:
                vencedor = 2
    if vencedor == 1:
        print("Você venceu")
    elif vencedor == 2:
        print("Computador venceu")
            
    return vencedor
          
def campeonato():
    ca_i=1
    placar_computador = 0
    placar_usuario = 0
    
    while ca_i <= 3:
        print("******* Rodada",ca_i,"*********")
        resultado_partida = partida()
        if resultado_partida == 1:
            placar_usuario = placar_usuario + 1
        elif resultado_partida == 2:
            placar_computador = placar_computador + 1
        ca_i = ca_i + 1
    print("Placar: Você",placar_usuario,"x",placar_computador,"Computador")
    
x = main()
