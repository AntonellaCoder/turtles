import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-300,-130)
t.pendown()
t.begin_fill()
while True:
    t.color('red', 'yellow')
    t.forward(600)
    t.left(130)
    if t.heading() == 0:
        break
t.end_fill()
turtle.done()

