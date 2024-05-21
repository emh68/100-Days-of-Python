import turtle
from turtle import Turtle, Screen
from random import randint

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(3):
    tim.forward(100)
    tim.right(120)
tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(4):
    tim.forward(100)
    tim.right(90)
tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(5):
    tim.forward(100)
    tim.right(72)
tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(6):
    tim.forward(100)
    tim.right(60)
tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(7):
    tim.forward(100)
    tim.right(51.43)
tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(8):
    tim.forward(100)
    tim.right(45)
tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(9):
    tim.forward(100)
    tim.right(40)


screen = Screen()
screen.exitonclick()
