# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen
import random

# Creacion del objeto de tipo tortuta
turtle = Turtle()

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.color('purple')
turtle.speed('fastest') # acelerar el dibujo

for i in range(500):
    turtle.forward(15)
    turtle.left(random.randint(0,360))
    turtle.forward(10)
    turtle.right(random.randint(0,180))
    # usando un numero aleatirio
    
# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()