from tkinter import *
import random

window = Tk()

window.geometry("300x300")
window.resizable(0, 0)
window.iconbitmap('cal2.ico')
window.title('generator')

nu1 = IntVar()
nu2 = IntVar()
nu3 = IntVar()

def pass_gene(len):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#$%&*?/+-"
    passwod = "".join(random.sample(char,len))
    result.delete(0, END)
    result.insert(0,passwod)

def checkbatta():
    if nu1.get()==6:
        pass_gene(6)
    elif nu2.get()==8:
        pass_gene(8)
    elif nu3.get()==10:
        pass_gene(10)
    else:
        pass_gene(7)


f1 = Frame(window, width=50, height=50, highlightbackground="White", highlightthickness=1)
f1.pack(side=TOP)

result = Entry(f1, width=25, font=('Dubai medium', 16), fg='Black', bg="White", justify=CENTER)
result.grid(row=0, column=0, ipady=30, columnspan=4)

f2 = Frame(window, width=20, height=10, bg="White")
f2.pack()

no1 = Checkbutton(f2, text='6 character', onvalue=6, offvalue=0, variable=nu1)
no1.grid(row=1, column=0)
no2 = Checkbutton(f2, text='8 character', onvalue=6, offvalue=0, variable=nu2)
no2.grid(row=2, column=0)
no3 = Checkbutton(f2, text='10 character', onvalue=6, offvalue=0, variable=nu3)
no3.grid(row=3, column=0)

gene = Button(f2,text='Generate',command = checkbatta)
gene.grid(row=4,column=0)

window.mainloop()
