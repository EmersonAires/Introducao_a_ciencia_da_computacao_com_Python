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



    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    tamanhoMedioPalavra = tamanho_medio_palavra(texto)
    relacaoTypeToken = relacao_Type_Token (texto)
    razaoHapaxLegomana = razao_Hapax_Legomana (texto)
    tamanhoMedioSentenca = tamanho_Medio_Sentenca(texto)
    complexidadeSentenca = complexidade_Sentenca(texto)
    tamanhoMedioFrase = tamanho_Medio_Frase(texto)

    return (tamanho_medio_palavra,relacaoTypeToken,razaoHapaxLegomana,tamanhoMedioSentenca,complexidadeSentenca,tamanhoMedioFrase)



def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

def tamanho_medio_palavra(texto):
    

    somaTamanhoPalavras = 0
    numeroTotalPalavras = 0
    lista_setencas = []
    lista_setencas = separa_sentencas(texto)
    for sentenca in lista_setencas:
        lista_frases = []
        lista_frases = separa_frases(sentenca)
        for frase in lista_frases:
            lista_palavras = []
            lista_palavras = separa_palavras(frase)
            numeroTotalPalavras = numeroTotalPalavras + len(lista_palavras)
            for palavra in lista_palavras:
                somaTamanhoPalavras = somaTamanhoPalavras + len(palavra)
    
    return (somaTamanhoPalavras/numeroTotalPalavras)


def relacao_Type_Token(texto):
    

    somaPalavrasDiferentes = 0
    numeroTotalPalavras = 0
    lista_setencas = []
    lista_setencas = separa_sentencas(texto)
    for sentenca in lista_setencas:
        lista_frases = []
        lista_frases = separa_frases(sentenca)
        for frase in lista_frases:
            lista_palavras = []
            lista_palavras = separa_palavras(frase)
            numeroTotalPalavras = numeroTotalPalavras + len(lista_palavras)
            somaPalavrasDiferentes = somaPalavrasDiferentes + n_palavras_diferentes(lista_palavras)
    
    print(somaPalavrasDiferentes/numeroTotalPalavras)
    return (somaPalavrasDiferentes/numeroTotalPalavras)






def razao_Hapax_Legomana(texto):


    numeroTotalPalavras = 0
    numeroTotalPalavrasUnicas = 0
    lista_setencas = []
    lista_setencas = separa_sentencas(texto)
    for sentenca in lista_setencas:
        lista_frases = []
        lista_frases = separa_frases(sentenca)
        for frase in lista_frases:
            lista_palavras = []
            lista_palavras = separa_palavras(frase)
            numeroTotalPalavras = numeroTotalPalavras + len(lista_palavras)
            numeroTotalPalavrasUnicas = numeroTotalPalavrasUnicas + n_palavras_unicas(lista_palavras)
           
    
    print(numeroTotalPalavrasUnicas/numeroTotalPalavras)
    return (numeroTotalPalavrasUnicas/numeroTotalPalavras)

def tamanho_Medio_Sentenca(texto):


    numeroCaracteresTotal = 0
    lista_setencas = []
    lista_setencas = separa_sentencas(texto)
    numeroSentencas = len(lista_setencas)
    for sentenca in lista_setencas:
        numeroCaracteresTotal = numeroCaracteresTotal + len(sentenca)
        
    return (numeroCaracteresTotal/numeroSentencas)



def complexidade_Sentenca(texto):


    lista_setencas = []
    lista_setencas = separa_sentencas(texto)
    numeroTotalSentencas = len(lista_setencas)
    numeroTotalFrases = 0
    for sentenca in lista_setencas:
        lista_frases = []
        lista_frases = separa_frases(sentenca)
        numeroTotalFrases = numeroTotalFrases + len(lista_frases)
        
    
    return (numeroTotalFrases/numeroTotalSentencas)


texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."


def tamanho_Medio_Frase(texto):


    numeroTotalCaracteres = 0
    numeroTotalFrases = 0
    lista_setencas = []
    lista_setencas = separa_sentencas(texto)
    for sentenca in lista_setencas:
        lista_frases = []
        lista_frases = separa_frases(sentenca)
        numeroTotalFrases = numeroTotalFrases + len(lista_frases)
        for frase in lista_frases:
            numeroTotalCaracteres = numeroTotalCaracteres + len(frase)
            
           
    return (numeroTotalCaracteres/numeroTotalFrases)


#calcula_assinatura(texto)
relacao_Type_Token(texto)
#razao_Hapax_Legomana("O gato caçava o rato")
#tamanho_medio_palavra(texto)