# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen

# Creacion del objeto de tipo tortuta
turtle = Turtle()

turtle.shape('turtle')
turtle.color("blue")
turtle.speed('fastest') # acelerar el dibujo


turtle.circle(50) # dibujar un circulo
turtle.setheading(56) # cambia la pocion de la tortuga
turtle.circle(50)
turtle.setheading(76)
turtle.circle(50)

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()