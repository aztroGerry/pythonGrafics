# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen, colormode
import random

# Creacion del objeto de tipo tortuta
turtle = Turtle()
turtle1 = Turtle()
turtle2 = Turtle()

# activar el formato rgb de colores 0 a 255
colormode(255)

# FUNCION PARA DETERMINAR EL COLOR AL ASAR
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb
    
    # Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.speed('fastest') # acelerar el dibujo

turtle1.shape('turtle')
turtle1.speed('fastest') # acelerar el dibujo

turtle2.shape('turtle')
turtle2.speed('fastest') # acelerar el dibujo

angulos = [0,90,180,270,360]

for i in range(500):
    turtle.color(random_color())
    turtle.forward(10)
    turtle.left(random.choice(angulos))
    turtle1.color(random_color())
    turtle1.forward(10)
    turtle1.left(random.choice(angulos))
    turtle2.color(random_color())
    turtle2.forward(10)
    turtle2.left(random.choice(angulos))
    # usando un numero aleatirio
    
# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()