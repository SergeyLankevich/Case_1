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
    Keyword argument: 
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
    Keyword argument: 
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
    Keyword argument: 
    x - x coordinate
    y - y coordinate
    """



def sun(x = 0, y = 0):



def picture_3():
    """
    #TODO: Painting the first picture using functions above: Ilya
    Keyword argument: 

    """

def picture_4():
    """
    #TODO: Painting the first picture using functions above: Ilya
    Keyword argument: 

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

house()

input('Press ENTER to exit')