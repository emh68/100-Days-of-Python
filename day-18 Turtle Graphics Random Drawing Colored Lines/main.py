import random
import turtle
import turtle as t
from turtle import Screen
from random import randint

tim = t.Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("blue")
tim.pensize(10)
screen = Screen()
def is_in_screen(w, tim):
    if random.random() > 0:
        return True
    else:
        return False

while is_in_screen(screen, tim):
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    steps = randint(0, 100)
    tim.forward(steps)
    turn = random.randrange(0, 2)
    if turn == 0:
        tim.left(90)
    else:
        tim.right(90)


screen.exitonclick()