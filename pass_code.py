import sqlite3

from tkinter import *

# database
with sqlite3.connect('password_vault.db') as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

# for windows
window = Tk()

window.iconbitmap('cal2.ico')
window.title('password manager')


def first_thing():
    window.geometry("300x150")

    labe = Label(window, text="Master Key")
    labe.config(anchor=CENTER)
    labe.pack()

    text1 = Entry(window, width=30, show="*")
    text1.pack()
    text1.focus()

    lab2 = Label(window, text="re_enter password")
    lab2.config(anchor=CENTER)
    lab2.pack()

    txt = Entry(window, width=30, show="*")
    txt.pack()
    txt.focus()

    buttn = Button(window, text='Submit', command=save)
    buttn.pack(pady=20)


def save():
    if text1.get() == txt.get():
        hashedPassword = text1.get()
        insert_password = """INSERT INTO MASTERPASSWORD(password)
        VALUES(?)"""
        cursor.execute(insert_password, [(hashedPassword)])
        db.commit()
        passwordVault()
    else:
        text1.delete(0, END)
        txt.delete(0, END)
        labe.config(text='password doesnt match')


def logins():
    window.geometry("400x200")

    lab = Label(window, text="Enter the passsword")
    lab.config(anchor=CENTER)
    lab.pack()

    text = Entry(window, width=30, show="*")
    text.pack()
    text.focus()

    buttn = Button(window, text='lets GO', command=checking)
    buttn.pack(pady=20)


def getMaster_pass():
    checkMaster_pass = text.get()
    cursor.execute('SELECT * FROM masterpassword WHERE id = 1 AND password = ?', [(checkMaster_pass)])
    return cursor.fetchall()


def checking():
    if match == getMaster_pass():
        print('hello')
        passwordVault()
    else:
        text.delete(0, END)
        lab.config(text="wrong password")


def passwordVault():
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("600x400")

    lab1 = Label(window, text='The password')
    lab1.config(anchor=CENTER)
    lab1.pack()


cursor.execute('SELECT * FROM masterpassword')
if cursor.fetchall():
    logins()
else:
    first_thing()

window.mainloop()
