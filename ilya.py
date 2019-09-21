import turtle
import math

def tri( edge, turn, color, x = 0, y = 0):          #edge - lenght of cathet
    turtle.up()                                     #turn - turn of triangle at clockwise
    turtle.setposition(x, y)                        #color - fill color of triangle
    turtle.setheading(0)                            #x - x coordinate of start
    turtle.down()                                   #y - y coordinate of start
    turtle.color(color)
    turtle.right(turn)
    turtle.begin_fill()
    turtle.fd(edge)
    turtle.left(135)
    turtle.fd(edge * math.sqrt(2))
    turtle.left(135)
    turtle.fd(edge)
    turtle.end_fill()

tri( 100, 0, '#D40000')
tri( 100, 90, '#D40000', 0 , -25)
tri( 100, 180, '#D40000', -25 , -25)
tri( 100, 270, '#D40000', -25 , 0)
input()