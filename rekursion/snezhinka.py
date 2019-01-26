import turtle

turtle.speed('fastest')
turtle.left(180)
turtle.penup()
turtle.forward(200)
turtle.left(180)
turtle.pendown()


def kokh(length: int, depth: int):
    if depth == 1:
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        return

    kokh(length, depth - 1)
    turtle.left(60)
    kokh(length, depth - 1)
    turtle.right(120)
    kokh(length, depth - 1)
    turtle.left(60)
    kokh(length, depth - 1)


def snezhinka(length: int, depth: int):
    for _ in range(3):
        kokh(length, depth)
        turtle.right(120)


snezhinka(2, 5)
