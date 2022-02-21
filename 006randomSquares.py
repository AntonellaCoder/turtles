import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
def rectangle(x, y):
    t.width(10)
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.penup()
    t.goto(random.randint(-300,300), random.randint(-300,300))
    t.pendown()
    angle = random.randint(0,360)
    t.screen.bgcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.begin_fill()
    t.setheading(angle)
    t.forward(x/2)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x/2)
    t.end_fill()

for i in range(1, 100):
    a = random.randint(20, 200)
    b = random.randint(20, 200)
    rectangle(a,b)

turtle.done()
