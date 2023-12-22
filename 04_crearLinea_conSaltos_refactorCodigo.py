# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen

# Creacion del objeto de tipo tortuta
turtle = Turtle()

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.color('purple')

# Comenzando a dibujar un cuadrado
for j in range (4):
    
    for i in range(5):
        turtle.forward(20) # escribir
        turtle.penup() # levantar el lapiz
        turtle.forward(20) # avanzar sin escribir
        turtle.pendown() # bajar la mano
    turtle.left(90)

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()