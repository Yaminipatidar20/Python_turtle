import turtle

t=turtle.Turtle()
t.speed(100)
turtle.bgcolor('black')

for i in range(250):
    t.color('magenta')
    t.circle(i)
    t.left(10)

turtle.done