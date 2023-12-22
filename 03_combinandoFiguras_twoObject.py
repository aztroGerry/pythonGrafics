# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen

# Creacion del objeto de tipo tortuta
turtle = Turtle()

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.color('purple')

# Comenzando a dibujar un cuadrado
turtle.forward(20) # escribir
turtle.penup() # levantar el lapiz
turtle.forward(20) # avanzar sin escribir
turtle.pendown() # bajar la mano
turtle.forward(20) # volver a escribir
turtle.penup() # levantar el lapiz
turtle.forward(20) # avanzar sin escribir
turtle.pendown() # bajar la mano
turtle.forward(20)
turtle.penup() # levantar el lapiz
turtle.forward(20) # avanzar sin escribir
turtle.pendown() # bajar la mano
turtle.forward(20)
turtle.penup() # levantar el lapiz
turtle.forward(20) # avanzar sin escribir
turtle.pendown() # bajar la mano
turtle.forward(20)
# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()