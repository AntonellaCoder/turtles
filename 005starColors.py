import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.penup()
t.goto(-300,-130)
t.pendown()
i=1
while True:
    t.begin_fill()
    while True:
        #print('inner: ', i)
        if i%3 == 0:
            break
        t.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)),(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        t.forward(600)
        t.left(130)
        i = i +1
    t.end_fill()
    i = i + 1
    if t.heading() == 0:
        break
turtle.done()
