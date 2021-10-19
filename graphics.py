from turtle import *

colors=['red','blue','green','purple','yellow','orange']
bgcolor('black')

for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)
    speed(11)