import turtle

turtle.speed('fastest')


def dragon(length: int, depth: int, direction: str):
    if depth == 1:
        if direction == 'left':
            turtle.right(45)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.right(45)
            return
        else:
            turtle.left(45)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(length)
            turtle.left(45)
            return
    turtle.right(45)
    dragon(length, depth - 1, 'left')
    turtle.left(90)
    dragon(length, depth - 1, 'right')
    turtle.right(45)


dragon(4, 10, 'left')
