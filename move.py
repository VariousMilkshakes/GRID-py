# -*- coding: cp1252 -*-
print "Welcome to the this Test"
print "This is test 2: Organic Grid!"
print

oY = input("How tall do you want your grid?")
oX = input("How wide do you want your grid?")
oY = oY - 1
oX = oX - 2

Xinput = input("Where do you want to start? (X)")
Yinput = input("Where do you want to start (Y)?")

mX = Xinput
mY = Yinput

game = 0
ship='^'

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

        del rowXdef[(oY + 1)]


        for line in rowXdef:
                x = rowXdef[line]
                cCell = 0
                while (cCell <= oX):
                        for cell in x:
                                print cell,
                                cCell = cCell + 1
                        print "\n"
        move = raw_input()
        clean = 0

        
        while (clean == 0):
                if move == 'w':
                        if mY != 0:
                                mY = mY - 1
                        else:
                                mY = Yinput
                        ship = '^'
                        clean = 1
                elif move == 'a':
                        if mX != 0:
                                mX = mX - 1
                        else:
                                mX = Xinput
                        ship = '<'
                        clean = 1
                elif move == 'd':
                        if mX != Xinput:
                                mX = mX + 1
                        else:
                                mX = 0
                        ship = '>'
                        clean = 1
                elif move == 's':
                        if mY != Yinput:
                                mY = mY + 1
                        else:
                                mY = 0
                        ship = 'v'
                        clean = 1
                else:
                        print "Ïnvalid Movement Key"
        

#Range Error?
#Button row doesn't exist
