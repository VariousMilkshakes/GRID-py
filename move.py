# -*- coding: cp1252 -*-
from random import randint
import sys

print "Welcome to the this Test"
print "This is test 2: Sam like Woffles!"
print

gY = input("How tall do you want your grid?")
gX = input("How wide do you want your grid?")
oY = gY
oX = gX - 2

Xinput = input("Where do you want to start? (X)")
Yinput = input("Where do you want to start (Y)?")
print


c = 0
while (c == 0):
        foodX = randint(0,oX)
        foodY = randint(0,oY)
        if Xinput == foodX and foodY == Yinput:
                c = 0
        else:
                c = 1

fX = foodX
fY = foodY

item = '#'

mX = Xinput
mY = Yinput

game = 0
ship='A'
jump = False

while(game == 0):
        o = 0
        x = 0
        y = 0
        rowXdef = {
                0 : [o]
                }

        while (y <= oY):
                while (x <= oX):
                         rowXdef[y].append(o)
                         x = x + 1
                x = 0
                y = y + 1
                rowXdef[y] = [o]

        mark = rowXdef[mY]
        mark[mX] = ship

        spawn = rowXdef[fY]
        spawn[fX] = item
        
        del rowXdef[(oY + 1)]
        del rowXdef[oY]

        if mY == fY and mX == fX:
                print 'WIN'
                raw_input()
                sys.exit()
                
        
        for line in rowXdef:
                x = rowXdef[line]
                cCell = 0
                while (cCell <= oX):
                        for cell in x:
                                print cell,
                                cCell = cCell + 1
                        print
        clean = 0
        
        while (clean == 0):
                move = raw_input()
                
                if move == 'w':
                        if jump == True:
                                mY = (gY - 1)
                                jump = False
                        else:
                                mY = mY - 1
                                if mY == 0:
                                        jump = True
                        ship = 'A'
                        clean = 1
                elif move == 'a':
                        if jump == True:
                                mX = (gX - 1)
                                jump = False
                        else:
                                mX = mX - 1
                                if mX == 0:
                                        jump = True
                        ship = '<'
                        clean = 1
                elif move == 'd':
                        if jump == True:
                                mX = 0
                                jump = False
                        else:
                                mX = mX + 1
                                if mX == (gX - 1):
                                        jump = True
                        ship = '>'
                        clean = 1
                elif move == 's':
                        if jump == True:
                                mY = 0
                                jump = False
                        else:
                                mY = mY + 1
                                if mY == (gY - 1):
                                        jump = True
                                ship = 'V'
                        clean = 1
                else:
                        print "Ïnvalid Movement Key"
