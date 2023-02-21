import turtle
import random
tao = turtle.Pen()
tao.shape("turtle")
tao.penup()

for item in range(20):
    getX = random.randrange(-200, 200)
    getY = random.randrange(-200, 200)
    tao.goto(getX, getY)
    tao.pendown()
    size = random.randrange(25, 200)
    for item in range(4):
        tao.forward(size)
        tao.left(90)
    tao.penup()

input("Exit")