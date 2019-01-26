import turtle

turtle.speed('fastest')
turtle.left(180)
turtle.penup()
turtle.forward(1000)
turtle.left(180)
turtle.pendown()


def kokh(length:int, depth:int):
    if depth == 1:
        turtle.forward(length)
        turtle.left(45)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(45)
        turtle.forward(length)
        return

    kokh(length, depth - 1)
    turtle.left(45)
    kokh(length, depth - 1)
    turtle.right(90)
    kokh(length, depth - 1)
    turtle.left(45)
    kokh(length, depth - 1)


kokh(2, 7)
