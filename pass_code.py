import hashlib
import sqlite3
from functools import partial

from tkinter import Button
from tkinter import CENTER
from tkinter import Entry
from tkinter import Label
from tkinter import TOP
from tkinter import Tk
from tkinter import simpledialog


# database code
with sqlite3.connect('password_vault.db') as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")


# Create PopUp
def popUp(text):
    answer = simpledialog.askstring("input string", text)
    print(answer)

    return answer


# Initiate root
root = Tk()
root.update()
root.iconbitmap('cal2.ico')

root.title("Password Vault")


def hashPassword(input):
    hash1 = hashlib.md5(input)
    hash1 = hash1.hexdigest()

    return hash1


def firstko():
    root.geometry('275x150')
    lab = Label(root, text="Choose a Master Password")
    lab.config(anchor=CENTER)
    lab.pack()

    txt = Entry(root, width=20, show="*")
    txt.pack()
    txt.focus()

    ob1 = Label(root, text="Re-enter the password")
    ob1.config(anchor=CENTER)
    ob1.pack()

    txt1 = Entry(root, width=20, show="*")
    txt1.pack()

    def save_pass():
        if txt.get() == txt1.get():
            hashedPassword = hashPassword(txt.get().encode('utf-8'))

            insert_password = """INSERT INTO masterpassword(password)
               VALUES(?) """
            cursor.execute(insert_password, [(hashedPassword)])
            db.commit()

            vaultScreen()
        else:
            ob1.config(text="Different passcode")

    btn = Button(root, text="Save", command=save_pass)
    btn.pack(pady=2)


def logbhitra():
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry('250x125')

    lab = Label(root, text="Master Password", fg='blue', font=("bold", 10))
    lab.config(anchor=CENTER)
    lab.pack()

    txt = Entry(root, width=20, show="*", justify='center', fg='blue')
    txt.pack()
    txt.focus()

    ob1 = Label(root)
    ob1.config(anchor=CENTER)
    ob1.pack(side=TOP)

    def getM_pass():
        checkHashedPassword = hashPassword(txt.get().encode('utf-8'))
        cursor.execute('SELECT * FROM masterpassword WHERE id = 1 AND password = ?', [(checkHashedPassword)])
        return cursor.fetchall()

    def checkPassword():
        password = getM_pass()

        if password:
            vaultScreen()
        else:
            txt.delete(0, 'end')
            ob1.config(text="Wrong Password")

    btn = Button(root, text="Submit", command=checkPassword, fg='blue')
    btn.pack(pady=5)


def vaultScreen():
    for widget in root.winfo_children():
        widget.destroy()

    def addEntry():
        text1 = "Website"
        text2 = "Username"
        text3 = "Password"
        website = popUp(text1)
        username = popUp(text2)
        password = popUp(text3)

        insert_fields = """INSERT INTO vault(website, username, password) 
        VALUES(?, ?, ?) """
        cursor.execute(insert_fields, (website, username, password))
        db.commit()

        vaultScreen()

    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()
        vaultScreen()

    root.geometry('800x600')
    root.resizable(0, 0)

    lab = Label(root, text="Password Vault")
    lab.grid(column=1)
    lab.config(anchor=CENTER)

    btn = Button(root, text="+", command=addEntry)
    btn.grid(row=1, column=1, padx=20, pady=10)

    lab = Label(root, text="Website")
    lab.grid(row=2, column=0, padx=80)
    lab = Label(root, text="Username")
    lab.grid(row=2, column=1, padx=80)
    lab = Label(root, text="Password")
    lab.grid(row=2, column=2, padx=80)

    cursor.execute('SELECT * FROM vault')
    if (cursor.fetchall() != None):
        i = 0
        while True:
            cursor.execute('SELECT * FROM vault')
            array = cursor.fetchall()

            if (len(array) == 0):
                break

            ob1 = Label(root, text=(array[i][1]), font=("Verdana", 12))
            ob1.grid(column=0, row=(i + 3))
            ob2 = Label(root, text=(array[i][2]), font=("Verdana", 12))
            ob2.grid(column=1, row=(i + 3))
            ob3 = Label(root, text=(array[i][3]), font=("Verdana", 12))
            ob3.grid(column=2, row=(i + 3))

            btn = Button(root, text="Delete", command=partial(removeEntry, array[i][0]))
            btn.grid(column=3, row=(i + 3), pady=10)

            i = i + 1

            cursor.execute('SELECT * FROM vault')
            if (len(cursor.fetchall()) <= i):
                break


cursor.execute('SELECT * FROM masterpassword')
if (cursor.fetchall()):
    logbhitra()
else:
    firstko()

root.mainloop()
