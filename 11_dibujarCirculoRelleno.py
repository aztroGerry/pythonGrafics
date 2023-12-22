# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen, colormode
import random

# Creacion del objeto de tipo tortuta
turtle = Turtle()

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')

colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

turtle.dot(65, random_color())

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()