import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    i = 0
    x = 0
    while i < 6 :
        x = x + abs(as_a[i] - as_b[i])
        i += 1

    grauSimilaridade = (x/6)

    return grauSimilaridade

def calcula_assinatura(texto):


    lista_sentenca = []
    lista_frases = []
    lista_palavras = []

    lista_sentenca = separa_sentencas(texto)
    for sentenca in lista_sentenca:
        lista_frases.extend(separa_frases(sentenca)) 
            
    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))
    
    somaTamanhoPalavras = 0
    numeroTotalPalavras = len(lista_palavras)

    for palavra in lista_palavras:
        somaTamanhoPalavras = somaTamanhoPalavras + len(palavra)

    tamanhoMedioPalavra = (somaTamanhoPalavras/numeroTotalPalavras) # 1ª Traço linguístico

    numeroPalavrasDiferentes = n_palavras_diferentes(lista_palavras)
    relacaoTypeToken = (numeroPalavrasDiferentes/numeroTotalPalavras) # 2ª Traço linguístico

    numeroPalavrasUnicas = n_palavras_unicas(lista_palavras)
    relacaoHapaxLegomana = (numeroPalavrasUnicas/numeroTotalPalavras) # 3ª Traço linguístico
    
    somaTotalNumeroCaracteresSentenca = 0
    NumeroSetenca = len(lista_sentenca)
    for sentenca in lista_sentenca:
        somaTotalNumeroCaracteresSentenca = somaTotalNumeroCaracteresSentenca + len(sentenca)

    tamanhoMedioSetenca = (somaTotalNumeroCaracteresSentenca/NumeroSetenca) # 4ª Traço linguístico

    numeroTotalFrases = len(lista_frases)
    complexidadeSetenca = (numeroTotalFrases/NumeroSetenca) # 5ª Traço linguístico

    numeroTotalFrases = len(lista_frases)
    somaCaracteresCadaFrase = 0
    for frase in lista_frases:
        somaCaracteresCadaFrase = somaCaracteresCadaFrase + len(frase)
    
    tamanhoMedioFrase = (somaCaracteresCadaFrase/numeroTotalFrases) # 6ª Traço linguístico

    lista_Assinatura = [tamanhoMedioPalavra, relacaoTypeToken, relacaoHapaxLegomana, tamanhoMedioSetenca, complexidadeSetenca, tamanhoMedioFrase]

    
    return lista_Assinatura
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    listaAssinaturas = []

    for texto in textos:
        listaAssinaturas.append(calcula_assinatura(texto))

    listaGrauSimilaridade = []
    for assinaturas in listaAssinaturas:
        listaGrauSimilaridade.append(compara_assinatura(assinaturas, ass_cp))

    grauReferencia = listaGrauSimilaridade[0]
    posicaoTexto = 1
    for grau in listaGrauSimilaridade:
        if grau < grauReferencia:
            grauReferencia = grau
            posicaoTexto = listaGrauSimilaridade.index(grau) + 1
    
    return posicaoTexto
    
   

def main():


    assinaturaCohPiah = le_assinatura()
    listaTextos = le_textos()
    textoPlagio = avalia_textos(listaTextos, assinaturaCohPiah)
    
    print("O autor do texto",textoPlagio,"está infectado com COH-PIAH")


main()