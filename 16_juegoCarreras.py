# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen, colormode
import random

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
screen.setup(600,600)

turtles =[]

y = -250
# creacion de varias tortugas
for i in range(14):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(random_color())
    new_turtle.goto(-280, y)
    y += 40
    turtles.append(new_turtle)

def jugar():
    final = False
    
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(1,10))
            if turtle.xcor()>250:
                turtle.write('Ganaste!!!', font=('Arial', 30, 'bold'))
                final = True
                break
        if final:
            break

screen.listen()
screen.onkey(key='space', fun = jugar)

screen.exitonclick()