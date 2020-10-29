"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange, randint
from turtle import *
from freegames import vector

#A01701879 María José Díaz Sánchez
#A00829556 Santiago Gonzalez Irigoyen
#Este código es un juego de tiro parabólico
#29 de octubre de 2020

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        #crear libreria de colores para los blancos
        #estos colores se usan para cambiar de manera aleatoria 
        #a los objetivos
        colors = ['cyan','yellow','light green','red','pink']
        t = randint(0,4)
        dot(20, colors[t])

    if inside(ball):
        #aquí se le da el color al proyectil
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(20) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        '''Aquí se regula el movimiento
        de los objetivos, al aumentar su
        movimiento en x aumenta si velocidad'''
        target.x -= 1.5

    if inside(ball):
        '''Aquí no se movió nada porque se notó 
        que esto acortaba la altura del proyectil'''
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return
    '''El ontimeter regula la velocidad del proyectil
    en este caso se cambio de 50 a 35 para hacer al juego
    más rápido'''
    ontimer(move, 35)

#aquí se crea el espacio del juego
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
#mientras 'True' sea 'True' (i.e. siempre), se corre move() en loop
while True:
    move()
done()
