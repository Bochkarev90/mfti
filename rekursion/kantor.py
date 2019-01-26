import turtle

depth = 13
y = 450
turtle.penup()
turtle.goto(-900, y)
turtle.pendown()


def kantor(length: int, depth: int):
    cut = length / 3
    if depth == 1:
        turtle.forward(cut)
        turtle.penup()
        turtle.forward(cut)
        turtle.pendown()
        turtle.forward(cut)
        return
    kantor(cut, depth - 1)
    turtle.penup()
    turtle.forward(cut)
    turtle.pendown()
    kantor(cut, depth - 1)


for i in range(depth):
    i += 1
    y -= 50
    kantor(1800, i)
    turtle.penup()
    turtle.goto(-900, y)
    turtle.pendown()
