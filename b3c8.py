import turtle
import random

colors = ["red","green","blue"]
painter = turtle.Turtle()
painter.pensize(10)
for i in range(4):
 for i in range(0,3):
    color = (colors)[i]
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0,0)