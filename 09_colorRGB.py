# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen, colormode
import random

# Creacion del objeto de tipo tortuta
turtle = Turtle()
turtle1 = Turtle()
turtle2 = Turtle()

# activar el formato rgb de colores 0 a 255
colormode(255)

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.color((123,54,67))
turtle.speed('fastest') # acelerar el dibujo

turtle1.shape('turtle')
turtle1.color((145,78,234))
turtle1.speed('fastest') # acelerar el dibujo

turtle2.shape('turtle')
turtle2.color((100,0,67))
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