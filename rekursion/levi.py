import turtle
import random

turtle.speed('fastest')


def levi(length: int, depth: int):
    if depth == 1:
        turtle.left(45)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(45)
        return
    turtle.left(45)
    levi(length, depth - 1)
    turtle.right(90)
    levi(length, depth - 1)
    turtle.left(45)


levi(20, 10)
