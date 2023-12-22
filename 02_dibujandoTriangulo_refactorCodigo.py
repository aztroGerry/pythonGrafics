# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen

# Creacion del objeto de tipo tortuta
turtle = Turtle()
turtle1 = Turtle()

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.color('purple')

turtle1.shape('turtle')
turtle1.color('blue')

# Comenzando a dibujar un cuadrado
for i in range(3):
    turtle.forward(200)
    turtle.left(120)

for i in range(4):
    turtle1.forward(200)
    turtle1.left(90)
    
turtle1.forward(25)

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()