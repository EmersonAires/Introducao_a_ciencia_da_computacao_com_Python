#range (início, fim, passo)

import turtle

wn = turtle.Screen()

wn.bgcolor("lightgreen")

tartaruga_1 = turtle.Turtle()

tartaruga_1.color("blue")

tartaruga_1.shape("turtle")

tartaruga_1.penup()   
                 
for size in range(5,60,2):      
    tartaruga_1.stamp()                
    tartaruga_1.forward(size)          
    tartaruga_1.right(24)              

wn.exitonclick()
