from turtle import *
from math import sqrt


def triangle_1( edge, turn, col, x = 0, y = 0):
    up()
    setposition(x, y)
    setheading(0)
    down()
    color(col)
    right(turn)
    begin_fill()
    fd(edge)
    left(135)
    fd(edge * sqrt(2))
    left(135)
    fd(edge)
    end_fill()

    """
    Done: Ilya
    Keyword arguments: 
    edge - lenght of cathet
    turn - turn of triangle at clockwise
    col - fill color of triangle
    x - x coordinate of start
    y - y coordinate of start
    """


def rectangle( edgex, edgey, col, x = 0, y = 0):
    up()
    setposition(x, y)
    setheading(0)
    down()
    color(col)
    begin_fill()
    fd(edgex)
    lt(90)
    fd(edgey)
    lt(90)
    fd(edgex)
    lt(90)
    fd(edgey)
    end_fill()

    """
    Done: Ilya
    Keyword arguments: 
    edgex - lenght x
    edgey - lenght y
    turn - turn of triangle at clockwise
    col - fill color of triangle
    x - x coordinate of start
    y - y coordinate of start
    """




def parallelogram(x, y, side_a, side_b, angle_a, color, direction, turn):
    """
    Function: Painting any quadrangle.
    Keyword argument: 
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param side_a: length of the first side
    :param side_b: length of the second side
    :param angle_a: Any angle in the quadrangle
    :param color: filling color
    :param direction: the direction quadrangle is facing towards (west/east)
    :param: turn of the triangle (clockwise)
    :return: None

    """
    up()
    setpos(x, y)
    down()
    begin_fill()
    fillcolor(color)
    left(turn)
    fd(side_a)
    left((180 - angle_a) * direction)
    fd(side_b)
    left((angle_a) * direction)
    fd(side_a)
    left((180 - angle_a) * direction)
    fd(side_b)
    left((angle_a - 90) * direction)
    end_fill()
    



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
    up()
    setposition(x, y)
    setheading(0)
    down()
    color('#FFDB00')

    begin_fill()
    circle(25)
    end_fill()

    angle = 5.74
    up()
    setposition(x, y + 30)
    setheading(0)
    down()

    begin_fill()
    fd(50)
    for i in range(36):
        rt(175)
        fd(100)

    end_fill()



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

def grass(x = 0, y = 0):
    for i in range(20):
        triangle_1(25, 135, '#006500', x + i * 25 * sqrt(2), y)

def ilya(x = 0, y = 0):
    house(x - 100, y)
    sun(x + 225, y+ 300)
    tree(x - 400, y)
    grass(x - 450, y + 15)
    flag(x - 225, y)

    """
    Done: Ilya
    Keyword arguments:
    x - x coordinate
    y - y coordinate
    """

def flower():
    """
    Function: painting a flower using only parallelogram function.
    Keyword argument: 
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param side_a: length of the first side
    :param side_b: length of the second side
    :param angle_a: Any angle in the quadrangle
    :param color: filling color
    :param direction: the direction quadrangle is facing towards (west/east)
    :param: turn of the triangle (clockwise)
    :return: None

    """
    parallelogram(0, 0, 75, 100, 135, '#FF4BE8', 1, 90)
    parallelogram(0, 0, 75, 100, 135, '#FF99FF', -1, 90)
    parallelogram(0, 0, 75, 100, 135, '#FF99FF', -1, 0)
    parallelogram(0, 0, 75, 100, 135, '#FF4BE8', 1, 90)
    parallelogram(0, 0, 75, 100, 135, '#FF4BE8', 1, 0)
    parallelogram(0, 0, 75, 100, 135, '#FF4BE8', 1, 0)  
    parallelogram(0, 0, 75, 100, 135, '#FF99FF', -1, -90)
    parallelogram(0, 0, 75, 100, 135, '#FF99FF', -1, 180)
    parallelogram(0, 75, 100, 100, 90, '#FF3333', 1, 45)
    parallelogram(-75, 0, 100, 100, 90, '#FF3333', 1, 180)
    parallelogram(75, 0, 100, 100, 90, '#FF3333', 1, -90)
    parallelogram(0, -75, 100, 100, 90, '#FF3333', 1, 0)
    parallelogram(100 / sqrt(2), 100 / sqrt(2), 75, 75, 90, '#C300D1', 1, -135)
    parallelogram(-100 / sqrt(2), 100 / sqrt(2), 75, 75, 90, '#C300D1', 1, 180)
    parallelogram(100 / sqrt(2), -100 / sqrt(2), 75, 75, 90, '#C300D1', 1, -90)
    parallelogram(-100 / sqrt(2), -100 / sqrt(2), 75, 75, 90, '#C300D1', 1, 0)
    parallelogram(100 / sqrt(2), 100 / sqrt(2) + 75, 75, 100, 135, '#FF0000', 1, 0)
    parallelogram(100 / sqrt(2), 100 / sqrt(2) + 75, 75, 100, 135, '#FF0000', -1, 90)
    parallelogram(100 / sqrt(2), 100 / sqrt(2) + 75, 75, 100, 135, '#E20000', 1, 180)
    parallelogram(100 / sqrt(2) + 75, 100 / sqrt(2), 75, 100, 135, '#E20000', -1, 180)
    parallelogram(100 / sqrt(2) + 75, 100 / sqrt(2), 75, 100, 135, '#CC0000', -1, 180)
    parallelogram(100 / sqrt(2) + 75, 100 / sqrt(2), 75, 100, 135, '#CC0000', 1, -90)
    parallelogram(100 / sqrt(2) + 75, -100 / sqrt(2), 75, 100, 135, '#CC0000', 1, 90)
    parallelogram(100 / sqrt(2) + 75, -100 / sqrt(2), 75, 100, 135, '#CC0000', -1, 90)
    parallelogram(100 / sqrt(2) + 75, -100 / sqrt(2), 75, 100, 135, '#CC0000', 1, 180)
    parallelogram(100 / sqrt(2) + 75, -100 / sqrt(2), 75, 100, 135, '#E20000', 1, 180)
    parallelogram(100 / sqrt(2), -100 / sqrt(2) - 75, 75, 100, 135, '#E20000', -1, 90)
    parallelogram(100 / sqrt(2), -100 / sqrt(2) - 75, 75, 100, 135, '#FF0000', 1, 180)
    parallelogram(100 / sqrt(2), -100 / sqrt(2) - 75, 75, 100, 135, '#FF0000', -1, 90)
    parallelogram(-100 / sqrt(2), -100 / sqrt(2) - 75, 75, 100, 135, '#FF6666', 1, 180)
    parallelogram(-100 / sqrt(2), -100 / sqrt(2) - 75, 75, 100, 135, '#FF6666', -1, 180)
    parallelogram(-100 / sqrt(2), -100 / sqrt(2) - 75, 75, 100, 135, '#FF6666', 1, -90)
    parallelogram(-100 / sqrt(2) - 75, -100 / sqrt(2), 75, 100, 135, '#FF9999', -1, 90)
    parallelogram(-100 / sqrt(2) - 75, -100 / sqrt(2), 75, 100, 135, '#FFCCCC', -1, 180)
    parallelogram(-100 / sqrt(2) - 75, -100 / sqrt(2), 75, 100, 135, '#FFCCCC', 1, -90)
    parallelogram(-100 / sqrt(2) - 75, 100 / sqrt(2), 75, 100, 135, '#FFCCCC', 1, 90)
    parallelogram(-100 / sqrt(2) - 75, 100 / sqrt(2), 75, 100, 135, '#FFCCCC', -1, 90)
    parallelogram(-100 / sqrt(2) - 75, 100 / sqrt(2), 75, 100, 135, '#FF9999', 1, 180)
    parallelogram(-100 / sqrt(2), 100 / sqrt(2) + 75, 75, 100, 135, '#FF9999', -1, 180)
    parallelogram(-100 / sqrt(2), 100 / sqrt(2) + 75, 75, 100, 135, '#FF6666', 1, 180)
    parallelogram(-100 / sqrt(2), 100 / sqrt(2) + 75, 75, 100, 135, '#FF6666', -1, 90)


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

speed(0)
ilya()


input('Press ENTER to exit')
