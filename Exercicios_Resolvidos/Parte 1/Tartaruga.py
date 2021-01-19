import turtle

wn = turtle.Screen()
corfundo = input("Digite a cor de fundo:")
wn.bgcolor(corfundo)         # define a cor de fundo da janela

tess = turtle.Turtle()

tess.shape("turtle")

corlinha = input("Digite a cor da linha:")

tess.color(corlinha)               # tess fica azul

espessuralinha = int(input("Digite a espessura da linha:"))

tess.pensize(espessuralinha)                  # define a espessura da caneta

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()