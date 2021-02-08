from tkinter import *
import sqlite3


def add():
    name = entry_name.get()
    grade = entry_grade.get()
    cursor.execute(""" INSERT INTO Scores(name, grade)
        VALUES(?, ?) """, (name, grade))
    db.commit()
    entry_name.delete(0, END)
    entry_grade.delete(0, END)
    entry_name.focus()


def clear():
    entry_name.delete(0, END)
    entry_grade.delete(0, END)
    entry_name.focus()

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Scores(
    id integer PRIMARY KEY,
    name text NOT NULL,
    grade integer); """)


window = Tk()
window.title("TestScores")
window.geometry("500x500")

label1 = Label(text = "Enter student's name: ")
label1.place(x = 30, y = 20)

entry_name = Entry(text ="")
entry_name.place(x = 200, y = 20)

label2 = Label(text = "Enter student's grade: ")
label2.place(x = 30, y = 50)

entry_grade = Entry(text ="")
entry_grade.place(x = 200, y = 50)

button_add = Button(text = "Add", command = add)
button_add.place(x = 200, y = 80)

button_clear = Button(text = "Clear", command = clear)
button_clear.place(x = 300, y = 80)

window.mainloop()