"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)


def speed():
    "The player can choose the speed of the game by means of this function"
    print("Bienvenido a Snake, para comenzar, tendrás lo opción de elegir la velocidad de la serpiente:")
    print("1. Lento")
    print("2. Medio")
    print("3. Rapido")
    x = int(input("¿Qué velocidad prefieres? = "))

    if x == 1:
        s = -10
    elif x == 2:
        s = -20
    elif x == 3:
        s = -30
    else:
        print("UPS, esa no es una opcion valida, selecciona una de las velocidades ingresando su número correspondiente.")
        exit

    return s


s = speed()     # speed
aim = vector(0, s)
snake = [vector(s * -1, 0)]


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def change_food(food):
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    # Si se encuentra a punto de chocar con el lado izquierdo/derecho del canvas
    if head.x == -190 or head.x == 180:
        if -200 < head.y < -5:
            "Left quadrant down"
            change(0, 10)
        if -5 < head.y < 190:
            "Right quadrant down"
            change(0, -10)

    # If it is about to collide with the bottom / top side of the canvas
    if head.y == -190 or head.y == 180:
        if -200 < head.x < -5:
            "Left quadrant down"
            change(10, 0)
        if -5 < head.y < 190:
            "Right quadrant down"
            change(-10, 0)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(s * -1, 0), 'Right')
onkey(lambda: change(s, 0), 'Left')
onkey(lambda: change(0, s * -1), 'Up')
onkey(lambda: change(0, s), 'Down')
onkey(lambda: change(s * -1, 0), 'd')
onkey(lambda: change(s, 0), 'a')
onkey(lambda: change(0, s * -1), 'w')
onkey(lambda: change(0, s), 's')
onkey(lambda: change_food(food), 'q')  # Change food location
move()
done()
