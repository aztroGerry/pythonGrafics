# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen
import random

# Creacion del objeto de tipo tortuta
turtle = Turtle()
turtle1 = Turtle()
turtle2 = Turtle()

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.color('purple')
turtle.speed('fastest') # acelerar el dibujo

turtle1.shape('turtle')
turtle1.color('blue')
turtle1.speed('fastest') # acelerar el dibujo

turtle2.shape('turtle')
turtle2.color('red')
turtle2.speed('fastest') # acelerar el dibujo

angulos = [0,90,180,270,360]

for i in range(500):
    turtle.forward(10)
    turtle.left(random.choice(angulos))
    turtle1.forward(10)
    turtle1.left(random.choice(angulos))
    turtle2.forward(10)
    turtle2.left(random.choice(angulos))
    # usando un numero aleatirio
    
# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()