from turtle import *

width(5)

color('green')
i = 0
while i < 100:
    forward(4)
    right(360/100)
    i = i + 1

penup()
right(180)
forward(150)
pendown()
color('yellow')

i = 0
while i < 100:
    forward(4)
    left(360/100)
    i = i + 1

penup()
setposition(-225, -50)
pendown()

right(180)

color('blue')
i = 0
while i < 100:
    forward(4)
    left(360/100)
    i = i + 1

penup()
setposition(-75, -50)
pendown()

color('black')

i = 0
while i < 100:
    forward(4)
    left(360/100)
    i = i + 1


penup()
setposition(75, -50)
pendown()

color('red')

i = 0
while i < 100:
    forward(4)
    left(360/100)
    i = i + 1


penup()

setposition(-225, -150)
color('black')
width(8)



done()