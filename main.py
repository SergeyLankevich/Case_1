import turtle
import math


def triangle_1( edge, turn, color, x = 0, y = 0):
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.down()
    turtle.color(color)
    turtle.right(turn)
    turtle.begin_fill()
    turtle.fd(edge)
    turtle.left(135)
    turtle.fd(edge * math.sqrt(2))
    turtle.left(135)
    turtle.fd(edge)
    turtle.end_fill()

    """
    Done: Ilya
    Keyword arguments: 
    edge - lenght of cathet
    turn - turn of triangle at clockwise
    color - fill color of triangle
    x - x coordinate of start
    y - y coordinate of start
    """


def rectangle( edgex, edgey, color, x = 0, y = 0):
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.fd(edgex)
    turtle.lt(90)
    turtle.fd(edgey)
    turtle.lt(90)
    turtle.fd(edgex)
    turtle.lt(90)
    turtle.fd(edgey)
    turtle.end_fill()

    """
    Done: Ilya
    Keyword arguments: 
    edgex - lenght x
    edgey - lenght y
    turn - turn of triangle at clockwise
    color - fill color of triangle
    x - x coordinate of start
    y - y coordinate of start
    """




def additional_figure_1():
    """
    #TODO: Paint and additional figure if needed: Ilya
    Keyword argument: 

    """


def additional_figure_2():
    """
    #TODO: Paint and additional figure if needed: Ilya
    Keyword argument: 

    """



def additional_figure_3():
    """
    #TODO: Paint and additional figure if needed: Ilya
    Keyword argument: 

    """


def additional_figure_4():
    """
    #TODO: Paint and additional figure if needed: Sergey
    Keyword argument: 

    """


def additional_figure_5():
    """
    #TODO: Paint and additional figure if needed: Sergey
    Keyword argument: 

    """


def additional_figure_6():
    """
    #TODO: Paint and additional figure if needed: Sergey
    Keyword argument: 

    """


def additional_figure_7():
    """
    #TODO: Paint and additional figure if needed: Sergey
    Keyword argument: 

    """

def house(x = 0, y = 0):

    #house
    rectangle(200, 200, '#E4A700', x, y)
    triangle_1(163, 135, '#910000', x + 100, y + 315)

    #window
    rectangle(50, 50, '#008ACC', x + 75, y + 75)
    rectangle(62, 6, '#2F1400', x + 69, y + 69)
    rectangle(6, 62, '#2F1400', x + 69, y + 69)
    rectangle(6, 62, '#2F1400', x + 125, y + 69)
    rectangle(62, 6, '#2F1400', x + 69, y + 125)
    rectangle(50, 6, '#2F1400', x + 75, y + 97)
    rectangle(6, 50, '#2F1400', x + 97, y + 75)

    """
    Done: Ilya
    Keyword arguments: 
    x - x coordinate
    y - y coordinate
    """



def sun(x = 0, y = 0):
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.down()
    turtle.color('#FFDB00')

    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    angle = 5.74
    turtle.up()
    turtle.setposition(x, y + 30)
    turtle.setheading(0)
    turtle.down()

    turtle.begin_fill()
    turtle.fd(50)
    for i in range(36):
        turtle.rt(175)
        turtle.fd(100)

    turtle.end_fill()



    """
    Done: Ilya
    Keyword arguments:
    x - x coordinate
    y - y coordinate
    """


def tree(x = 0 , y = 0):

    rectangle(30, 150, '#502400', x, y)
    rectangle(200, 175, '#006500', x - 85, y + 150)
    rectangle(50, 15, '#502400', x + 30, y + 100)
    rectangle(15, 35, '#502400', x + 65, y + 115)
    rectangle(150, 150, '#006500', x - 20, y + 190)

    """
    Done: Ilya
    Keyword arguments:
    x - x coordinate
    y - y coordinate
    """

def flag(x = 0, y = 0):

    rectangle(5, 175, '#502400', x, y)
    rectangle(20, 20, '#A50021', x + 5, y + 155)
    rectangle(20, 20, '#A50021', x + 5, y + 125)
    rectangle(30, 20, '#A50021', x + 35, y + 155)
    rectangle(30, 20, '#A50021', x + 35, y + 125)
    triangle_1(20, 90, '#A50021', x + 65, y + 175)
    triangle_1(20, 0, '#A50021', x + 65, y + 125)

    """
    Done: Ilya
    Keyword arguments:
    x - x coordinate
    y - y coordinate
    """

def ilya(x = 0, y = 0):
    house(x - 100, y)
    sun(x + 225, y+ 300)
    tree(x - 400, y)
    flag(x - 225, y)

    """
    Done: Ilya
    Keyword arguments:
    x - x coordinate
    y - y coordinate
    """

def picture_5():
    """
    #TODO: Painting the first picture using functions above: Sergey
    Keyword argument: 

    """


def picture_6():
    """
    #TODO: Painting the first picture using functions above: Sergey
    Keyword argument: 

    """


def picture_7():
    """
    #TODO: Painting the first picture using functions above: Sergey
    Keyword argument: 

    """



def picture_8():
    """
    #TODO: Painting the first picture using functions above: Sergey
    Keyword argument: 

    """



def picture_9():
    """
    #TODO: Painting the first picture using functions above: Sergey
    Keyword argument: 

    """


###############################################################################################

turtle.speed(0)
ilya()


input('Press ENTER to exit')