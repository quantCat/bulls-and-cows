#!/usr/bin/env python3
from tkinter import *
from random import *

bk = Tk ()
a1 = a2 = a3 = a4 = None
puzzle = None

def start():
    global a1, a2, a3, a4, move_cnt, puzzle
    a1 = randint(1, 9)
    a2 = a1
    while (a2 == a1):
        a2 = randint(0, 9)
    a3 = a1
    while (a3 == a1 or a3 == a2):
        a3 = randint(0, 
		     
		     9)
    a4 = a1
    while (a4 == a1 or a4 == a2 or a4 == a3):
        a4 = randint(0, 9)
    puzzle = a1*1000 + a2*100 + a3*10 + a4
    answer = 0
    move_cnt = 1
    history.configure (state='normal')
    history.delete('1.0', END)
    enter.delete (0, END)
    pwyn.config (text = "Please write your number")
    history.configure (state='disabled')

def show_answer():
    if puzzle is None:
        history.insert(END, "ERROR: Game not started\n")
        history.configure (state='disabled')
        return
    history.configure (state='normal')
    history.insert(END, "Answer is "+str(puzzle)+"\n")
    history.insert(END, "Do you wanna start a new game?\n")
    history.configure (state='disabled')
    

def destroy():
    bk.destroy()


def game(*_):
    history.configure (state='normal')
    global move_cnt
    if a1 is None:
        history.insert(END, "ERROR: Game not started\n")
        history.see(END)
        history.configure (state='disabled')
        return
    try:
        answer = int(enter.get (), 10)
    except ValueError:
        history.insert(END, "ERROR: This is not an integer number\n")
        history.see(END)
        history.configure (state='disabled')
        return
    if answer < 0 or answer > 9999:
        history.insert(END, "ERROR: Invalid number\n")
        history.see(END)
        history.configure (state='disabled')
        return
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
    history.insert(END, "{} - {}: Bulls = {} Cows = {}\n".format(
        move_cnt, answer, bulls, cows))
    move_cnt += 1
    if (answer == puzzle):
        history.insert(END, "You win!\n")
        history.insert(END, "Do you wanna start a new game?\n")
    enter.delete (0, END)
    history.see(END)
    history.configure (state='disabled')


newgamebutton = Button (bk, text="New game", command=start, cursor="hand2", height=1)
answerbutton = Button (bk, text="Show answer", command=show_answer, cursor="hand2", height=1)
quitbutton = Button (bk, text="Quit game", command=destroy, cursor="hand2", height=1)
history = Text (bk, height=15)
scrollhis = Scrollbar (bk)
scrollhis['command'] = history.yview
history['yscrollcommand'] = scrollhis.set
pwyn = Label (bk, text = "Please press 'New gawe' button")
enter = Entry (bk, width = 100)
enter.bind('<Return>', game)

newgamebutton.grid (row = 1, column = 1)
answerbutton.grid (row = 1, column = 2)
quitbutton.grid (row = 1, column = 3)
history.grid (row = 2, column = 1, columnspan = 3)
scrollhis.grid (row = 2, column = 4, sticky = W+N+S)
pwyn.grid (row = 3, column = 1, columnspan = 4)
enter.grid (row = 4, column = 1, columnspan = 4)

bk.mainloop()
