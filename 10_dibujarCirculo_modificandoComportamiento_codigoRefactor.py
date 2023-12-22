# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen, colormode
import random

# Creacion del objeto de tipo tortuta
turtle = Turtle()

turtle.shape('turtle')
turtle.speed('fastest') # acelerar el dibujo

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
        turtle.circle(100) # dibujar un circulo
        turtle.setheading(turtle.heading() + angle) # cambia la pocion de la tortuga

draw(int(input('Anota los grados: ')))

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()