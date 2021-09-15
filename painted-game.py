"""
How to play:
    At the begining you will have the shape of a line, to change the shape you can type the letter assigned
    to the letter you want to choose. 
    Shape options:  l -> line
                    s -> square
                    c -> circle
                    r -> rectangle
                    t -> triangle
    If you want to draw a shape click on the part of the screen where you want to start the shape, then click
    where you want it to end.

    To change of colors type one of the following options that are available for you in Uppercase.
    Color options:  K -> black
                    W -> white
                    G -> green
                    B -> blue
                    R -> red
                    P -> purple
                    O -> orange
"""

from turtle import *
from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(180):
        forward(end.x - start.x)
        left(2)

    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Multiplica por 2 para tener un lado doble de largo
    forward((2 * end.x) - start.x)
    left(90)
    forward(end.x - start.x)
    left(90)
    # Multiplica por 2 para tener un lado doble de largo
    forward((2 * end.x) - start.x)
    left(90)
    forward(end.x - start.x)
    left(90)

    end_fill()


# Funcion creada por Eduardo Acosta A01375206
def triangle(start, end):
    """Draw triangle from start to end."""
    # Definimos los puntos en el lienzo mediante los clics
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # Se utiliza rango 3 porque es el número de lados de un triangulo
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
# Colors you can choose by typing the avialable letter in Uppercase
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('orange'), 'O')
# Shapes you can choose by typing the avialable letters in lowercase
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
