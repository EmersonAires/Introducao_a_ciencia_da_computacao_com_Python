import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("yellow")
tess.shape("turtle")

print(range(5,60,2))
tess.penup()                    # isso é novo
for size in range(5,60,2):      # começar com size = 5 e passo 2
    tess.stamp()                # deixar um carimbo no canvas
    tess.forward(size)          # tess, vá para frente
    tess.right(24)              # tess, vire 24 graus a direita

wn.exitonclick()