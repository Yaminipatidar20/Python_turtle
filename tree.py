import turtle as tu

fo=tu.Turtle()
fo.left(150)
fo.speed(40)

def draw(i):
    if(i<10):
        return
    else:
        fo.forward(i)
        fo.left(30)
        draw(3*i/4)
        fo.right(60)
        draw(3*i/4)
        fo.left(30)
        fo.backward(i)

draw(150)
