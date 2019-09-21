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

def sqr( edgex, edgey, color, x = 0, y = 0):        #edgex - lenght x
    turtle.up()                                     #edgey - lenght y
    turtle.setposition(x, y)                        #turn - turn of triangle at clockwise
    turtle.setheading(0)                            #color - fill color of triangle
    turtle.down()                                   #x - x coordinate of start
    turtle.color(color)                             #y - y coordinate of start
    turtle.begin_fill()
    turtle.fd(edgex)
    turtle.rt(90)
    turtle.fd(edgey)
    turtle.rt(90)
    turtle.fd(edgex)
    turtle.rt(90)
    turtle.fd(edgey)
    turtle.end_fill()

turtle.speed(10)
tri( 100, 0, '#D40000')
tri( 100, 90, '#D40000', 0 , -25)
tri( 100, 180, '#D40000', -25 , -25)
tri( 100, 270, '#D40000', -25 , 0)

tri( 25, 135, '#00A300', -180 , -200)
tri( 25, 135, '#00A300', -180 + 40 , -200)
tri( 25, 135, '#00A300', -180 + 80 , -200)
tri( 25, 135, '#00A300', -180 + 120 , -200)
tri( 25, 135, '#00A300', -180 + 160 , -200)
tri( 25, 135, '#00A300', -180 + 200 , -200)
tri( 25, 135, '#00A300', -180 + 240 , -200)
tri( 25, 135, '#00A300', -180 + 280 , -200)
tri( 25, 135, '#00A300', -180 + 320 , -200)
tri( 25, 135, '#00A300', -180 + 360 , -200)

sqr(200, 100, '#E4A700', 150)

input()