'''
1st version

import csv
from datetime import datetime


def add_msg(name, msg):
    file_pointer = open("Chat.csv", "a")
    writer = csv.writer(file_pointer)
    writer.writerow([name, msg, datetime.now()])
    file_pointer.close()

def display_msgs():
    file_pointer = open("Chat.csv", "r")
    rows = list(csv.reader(file_pointer))
    length = len(rows)
    i = 0
    while i < length:
        name = rows[i][0]
        message = rows[i][1]
        date = rows[i][2][11:-7]
        output = name + "[ " + date + "]" + ": " + message
        print(output)
        i += 1



name = input("What is your name? ")
display_msgs()


while True:
    msg1 = input("Please add your message: ")
    add_msg(name, msg1)
    print("\n\n\n\n\n")
    display_msgs()


'''

from tkinter import *
import csv
import time

# tic = time.perf_counter()

# toc = time.perf_counter


def send_save_msg():

    chat_name = name_entrybox.get()
    msg = message_entrybox.get()

    chat_body.insert(END, chat_name + ":" + msg + "\n")
    message_entrybox.delete(0, END)

    file = open("chat_main.csv", "a")
    newrecord = chat_name + ":" + msg + "\n"
    file.write(newrecord)
    file.close()


def display_msg():
    clear()
    file = open("chat_main.csv", "r")
    rows = list(csv.reader(file))
    last_10 = rows[-10:]
    chat_body.insert(END, *last_10)
    message_entrybox.focus()
    

def clear():
    chat_body.delete(0, END)
    message_entrybox.focus()


def update_messages():
    display_msg()
    window.after(1000, update_messages)

window = Tk()
window.title("Chat")
window.geometry("530x520")

label_name = Label(text = "Enter your name")
label_name.place (x = 30, y = 30) 

name_entrybox = Entry(text = "")
name_entrybox.place(x = 30, y = 50, width = 100, height = 25)

label_msg = Label(text = "Enter your message")
label_msg.place (x = 30, y = 290) 

chat_body = Listbox()
chat_body.place(x = 30, y = 80, width = 300, height = 200)

message_entrybox = Entry(text = "")
message_entrybox.place(x =30, y = 320, width = 300, height = 60)

send_button = Button(text = "Send", command = send_save_msg)
send_button.place(x = 350, y = 320) 

display_msgs_button = Button(text= "Display all messages", command = display_msg)
display_msgs_button.place(x = 350, y = 150) 

clear_button = Button(text = "Clear the messages", command = clear)
clear_button.place(x = 350, y = 250)
        


update_messages()
window.mainloop()




