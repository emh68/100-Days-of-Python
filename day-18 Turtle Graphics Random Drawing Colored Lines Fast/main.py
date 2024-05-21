import turtle as t
import random
from turtle import Screen
from random import randint

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(10)
tim.speed("fastest")
screen = Screen()

direction = [0, 90, 180, 270]

for _ in range(200):
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    steps = randint(0,50)
    tim.forward(steps)
    tim.setheading(random.choice(direction))


screen.exitonclick()