import random

import pyperclip
from tkinter import *

root = Tk()
global passwod

root.geometry("300x300")
root.resizable(0, 0)
root.iconbitmap('cal2.ico')
root.title('generator')

def pass_gene(len):
    global passwod
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#$%&*?/+-"
    passwod = "".join(random.sample(char, len))
    print(passwod)
    result.delete(0, END)
    result.insert(0, passwod)


def checkbatta():
    if nu1.get() == 6 :
        pass_gene(6)
    if nu2.get() == 8:
        pass_gene(8)
    if nu3.get() == 10:
        pass_gene(10)

def clip():
    pyperclip.copy(passwod)

nu1 = IntVar()
nu2 = IntVar()
nu3 = IntVar()


f1 = Frame(root, width=50, height=50, highlightbackground="White", highlightthickness=1)
f1.pack(side=TOP)

result = Entry(f1, width=25, font=('Dubai medium', 16), fg='Black', bg="White", justify=CENTER)
result.grid(row=0, column=0, ipady=30, columnspan=4)

f2 = Frame(root, width=20, height=10, bg="White")
f2.pack()

no1 = Checkbutton(f2, text='6 character', onvalue=6, offvalue=0, variable=nu1)
no1.grid(row=1, column=0)


no2 = Checkbutton(f2, text='8 character', onvalue=8, offvalue=0, variable=nu2)
no2.grid(row=2, column=0)
no3 = Checkbutton(f2, text='10 character', onvalue=10, offvalue=0, variable=nu3)
no3.grid(row=3, column=0)

gene = Button(f2, text='Generate',fg= 'black',bg='yellow', command=checkbatta)
gene.grid(row=4, column=0)

copy = Button(f2, text='Copy', command=clip)
copy.grid(row=5, column=0)

root.mainloop()
