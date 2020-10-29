from random import randrange
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
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        '''Aquí se regula el movimiento 
        de los objetivos, al aumentar su
        movimiento en x aumenta si velocidad'''
        target.x -= 1.5

    if inside(ball):
        '''Aquí no se cambio nada porque se notó
        que eso disminuye la altura del proyectil'''
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
en este caso se cambio de 50 a 35 para hacer al proyectil
más rápido'''
    ontimer(move, 35)

#En estos comandos se prepara el área de juego
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
