# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen, colormode
import random

# Creacion del objeto de tipo tortuta
turtle = Turtle()
turtle1 = Turtle()

turtle.shape('turtle')
turtle.speed('fastest') # acelerar el dibujo

turtle1.shape('turtle')
turtle1.speed('fastest') # acelerar el dibujo

colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

def draw(angle):
    for i in range(int(360/angle)):
        turtle.color(random_color())
        turtle1.color(random_color())
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
        for i in range(3):
            turtle1.forward(100)
            turtle1.left(120)
        turtle.setheading(turtle.heading() + angle)
        turtle1.setheading(turtle.heading() + angle + 3)

draw(int(input('Anota los grados: ')))

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()