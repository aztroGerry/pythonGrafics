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

# ocultar a la tortuga
turtle.hideturtle()

for i in range(50):
    turtle.dot(65, random_color()) # dibujar con relleno
    turtle.goto(random.randint(-300,300), random.randint(-300,300)) # mover la posicion de la tortuga
                

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()