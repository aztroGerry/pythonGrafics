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

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()


# determinar el tamanio de la escena
screen.setup(500,500)

def move():
    turtle.forward(100)

def gira():
    turtle.left(90)
    
# creacion de varias tortugas
for i in range(5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(random_color())
    new_turtle.goto(random.randint(-300,300),random.randint(-300,300))
    
# detectar o escuchar al teclado o raton
screen.listen() # escuchador
screen.onkey(key='space', fun = move) # detectar el evento y realizar una accion
screen.onkey(key='z', fun = gira)

screen.exitonclick()