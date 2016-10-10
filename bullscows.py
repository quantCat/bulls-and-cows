#!/usr/bin/env python3

from random import *

a1 = randint(1, 9)
a2 = a1
while (a2 == a1):
    a2 = randint(0, 9)
a3 = a1
while (a3 == a1 or a3 == a2):
    a3 = randint(0, 9)
a4 = a1
while (a4 == a1 or a4 == a2 or a4 == a3):
    a4 = randint(0, 9)

puzzle = a1*1000 + a2*100 + a3*10 + a4
answer = 0
while (answer != puzzle):
    answer = int(input ("Please write your number - "))
    bulls = 0
    cows = 0
    b4 = answer % 10
    b3 = (answer // 10) % 10
    b2 = (answer // 100) % 10
    b1 = answer // 1000
    if (a1 == b1):
        bulls += 1
    if (a2 == b2):
        bulls += 1
    if (a3 == b3):
        bulls += 1
    if (a4 == b4):
        bulls += 1
    if (a1 == b2 or a1 == b3 or a1 == b4):
        cows += 1
    if (a2 == b1 or a2 == b3 or a2 == b4):
        cows += 1
    if (a3 == b1 or a3 == b2 or a3 == b4):
        cows += 1
    if (a4 == b1 or a4 == b2 or a4 == b3):
        cows += 1
    print ("Bulls - ", bulls, "Cows - ", cows)
