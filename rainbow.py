import turtle as t
import colorsys
t.speed(0)
t.hideturtle()
t.title("rainbow")
t.bgcolor("black")
t.setup(700,700)
colors=["blue", "pink", "violet", "Red", "green", "yellow"]
radius=300
penwidth=57
def draw(x,y,r,pensize,color):
    t.up()
    t.goto(x+r,y)
    t.down()
    t.seth(90)
    t.pensize(pensize)
    t.pencolor(color)
    t.circle(r,180)
for i in colors:
    draw(0,-100,radius,penwidth,i)
    radius-=(penwidth-1)
