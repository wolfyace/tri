import turtle
import random
wn=turtle.Screen()
t=turtle.Turtle()
t.turtlesize(0.1)


def midpt(ax,ay,bx,by):
    mx=(ax+bx)*(1/2)
    my=(ay+by)*(1/2)
    return mx, my

def fractal(n) -> object:
    ax=-200
    y_bottom=-200
    bx=200
    cx=0
    y_top=200
    t.penup()
    t.goto(ax,y_bottom)
    t.pendown()
    t.stamp()
    t.goto(bx,y_bottom)
    t.stamp()
    t.goto(cx,y_top)
    t.stamp()
    t.goto(ax,y_bottom)
    rx=0
    ry=random.uniform(y_top,y_bottom)
    t.penup()
    t.goto(rx,ry)
    t.pendown()
    t.stamp()
    a=(ax,y_bottom)
    b=(bx,y_bottom)
    c=(cx,y_top)
    pts=[a,b,c]
    for i in range(n):
        p=random.choice(pts)
        px=p[0]
        py=p[1]
        mid=midpt(px,py,rx,ry)
        t.penup()
        t.goto(mid)
        t.pendown()
        t.stamp()
        r=mid
        rx=r[0]
        ry=r[1]

if __name__=="__main__":
    fractal(100000)