# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen

# Creacion del objeto de tipo tortuta
turtle = Turtle()

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.color('purple')

# Comenzando a dibujar un cuadrado
for i in range(3):
    turtle.forward(200)
    turtle.left(120)


# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()