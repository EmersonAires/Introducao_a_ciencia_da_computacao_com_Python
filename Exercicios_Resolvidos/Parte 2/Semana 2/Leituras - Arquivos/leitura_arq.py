nome = "C:\\Users\\emerson eduardo\\Desktop\\Engenharia Civil\\hino.txt"   # poderia ser um input("Digite o nome do arquivo: ")

with open(nome, 'r', encoding='utf-8') as arq_entrada:
    # CORPO DO WITH
    conteudo = arq_entrada.read()

# continue o programa usando conteudo
print(conteudo)