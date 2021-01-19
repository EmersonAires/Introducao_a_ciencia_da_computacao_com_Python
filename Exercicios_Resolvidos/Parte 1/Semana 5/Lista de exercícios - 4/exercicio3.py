def vogal(letra):
    teste = 0
    for n in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
        if letra == n:
            teste = teste + 1
    return teste == 1
