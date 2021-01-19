x1 = float(input("Insira a coordenada x1: "))
y1 = float(input("Insira a coordenada y1: "))
x2 = float(input("Insira a coordenada x2: "))
y2 = float(input("Insira a coordenada y2: "))

import math

dxy = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if dxy >= 10 :
    print("longe")
else :
    print("perto")