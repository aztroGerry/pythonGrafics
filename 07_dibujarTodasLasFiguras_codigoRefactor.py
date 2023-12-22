# Importando la libreria que se esta utilizando de TURTLE
from turtle import Turtle, Screen

# Creacion del objeto de tipo tortuta
turtle = Turtle()

# Dibujando al objeto tortuga con un color definido
turtle.shape('turtle')
turtle.color('purple')

# Comenzando a dibujar un cuadrado
def draw(lados):

    for j in range (lados):
        
        for i in range(5):
            turtle.forward(5) # escribir
            turtle.penup() # levantar el lapiz
            turtle.forward(5) # avanzar sin escribir
            turtle.pendown() # bajar la mano
            
        turtle.left(360/lados)

# ciclo para correr la funcion para dibujar los numeros

for contador in range(3, 10):
draw(contador)

# Crear la escena y permitir que se cierre al dar un click
screen = Screen()
screen.exitonclick()