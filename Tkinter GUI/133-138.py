
'''
from tkinter import *

def click():
    sel = selectName.get()
    
    if sel == "Dick":
        photo = PhotoImage(file = "/Users/marina/workspace/100daysofcode/Tkinter GUI/the_cat1.gif")
        photobox.image = photo
    elif sel == "Sue":
        photo = PhotoImage(file = "/Users/marina/workspace/100daysofcode/Tkinter GUI/the_cat2.gif")
        photobox.image = photo
    elif sel == "Leopoldo":
        photo = PhotoImage(file = "/Users/marina/workspace/100daysofcode/Tkinter GUI/the_cat3.gif")
        photobox.image = photo

    photobox["image"] = photo
    photobox.update()

window = Tk()
window.title("Cats rule the world")
window.geometry("500x500")

window.wm_iconbitmap("./Tkinter GUI/icons/girl.ico")

window.configure(background = "light green")

logo = PhotoImage(file = "./Tkinter GUI/the_cat.gif")
logoimage = Label(image = logo)
logoimage.place(x = 30, y = 20, width = 200, height = 200)

photo = PhotoImage(file = "./Tkinter GUI/the_cat.gif" )
photobox = Label(window, image = photo)

photobox.image = photo
photobox.place(x = 30, y = 30, width = 200, height = 200)

selectName = StringVar(window)
selectName.set("Select Name")
namesList = OptionMenu(window, selectName, "Dick", "Sue", "Leopoldo")
namesList.place(x = 30, y = 250)

button_display_pics = Button(text = "click here", command = click)
button_display_pics.place(x = 200, y = 250)

window.mainloop()

'''


'''
Task 134

1. generate 2 random numbers between 10-50
2. type an answer of the sum of these numbers
3. if correct -> display image (e.g. a tick)
4. if wrong -> display image (e.g.a cross)
5. create "next" button to get another question



from tkinter import *
import random


def check_answer():

    user_answ= int(answerbox.get())
  
    num1 = int(numbox1["text"])
    num2 = int(numbox2["text"])

    answer = num1 + num2

    if user_answ == answer:
        img = PhotoImage(file = "./Tkinter GUI/correct.gif")
        imgbx.image = img
    else:
        img = PhotoImage(file = "./Tkinter GUI/wrong.gif")
        imgbx.image = img
    imgbx["image"] = img
    imgbx.update()    


def next_question():
    answerbox.delete(0, END)
    num1 = random.randint(10,50)
    num2 = random.randint(10,50)
    numbox1["text"] = num1
    numbox2["text"] = num2
    img = PhotoImage(file = "")
    imgbx.image = img
    imgbx["image"] = img
    imgbx.update()


window = Tk()
window.geometry("500x500")
window.title("calculate the sum")


numbox1 = Label(text = "0")
numbox1.place(x = 30, y = 20, width = 25, height = 25)

addsymbl = Message(text = "+")
addsymbl.place(x = 75, y = 20, width = 25, height = 25)

numbox2 = Label(text = "0")
numbox2.place(x = 100, y = 20, width = 25, height = 25)


eqlsymb = Message(text = "=")
eqlsymb.place(x = 125, y = 20, width = 25, height = 25)


answerbox = Entry(text = "")
answerbox.place(x = 150, y = 20, width = 25, height = 25)
answerbox.focus()

check_button = Button(text = "Check", command = check_answer )
check_button.place (x = 200, y = 20, width = 65, height = 25)


next_button = Button(text = "Next", command = next_question)
next_button.place(x = 280, y = 20, width = 65, height = 25)

img = PhotoImage(file = "")
imgbx = Label(image = img)
imgbx.image = img
imgbx.place(x = 30, y = 100, width = 200, height = 150)

window.mainloop()


'''
'''
Task 135

1. create dropdownlist
2. it should contain clikc me buttons with colors
3. upon click  -> the background color changes as the coor chosen


from tkinter import *

def click():
    sel = select_color.get()
    window.configure(background = sel)


window = Tk()
window.title("Colorful window")
window.geometry("300x300")


select_color = StringVar(window)
select_color.set("Select Color")

color_list = OptionMenu(window, select_color, "purple", "light blue", "violet", "light green")
color_list.place(x = 30, y = 25)

button_change_clr = Button(text = "click here", command = click)
button_change_clr.place(x = 200, y = 250)

window.mainloop()

'''
'''
Task 136

1. Enter a name (label + entry box)

2. Drop-down list with genders

3. Button "add" to a listbox name , gender

'''

# from tkinter import *

# def add_to_listbox():

#     name = enter_name.get()
#     enter_name.delete(0, END)
    
#     gender = select_gender.get()
#     select_gender.set("Select gender")

#     new_data = name + "," + gender + "\n"
#     names_list.insert(END, new_data)
#     enter_name.focus()



# window = Tk()
# window.title("Name + gender")
# window.geometry("500x500")

# label_name = Label(text = "Enter a name: ")
# label_name.place(x = 30, y = 20, width = 100, height = 25)

# enter_name = Entry(text = "")
# enter_name.place (x = 150, y = 20, width = 100, height = 25)

# select_gender = StringVar(window)
# select_gender.set("Select gender")

# gender_list = OptionMenu(window, select_gender, "Man", "Woman", "Other")
# gender_list.place(x = 30, y = 70)


# button_add = Button(text = "Add", command = add_to_listbox)
# button_add.place(x = 175, y = 70)


# names_list = Listbox()
# names_list.place(x = 30, y = 120, width = 130, height = 80)



# window.mainloop()



'''
from tkinter import *


window = Tk()
window.title("Chatter")


messages_frame = Frame(window)
my_msg = StringVar()

my_msg.set("Type yyour messages here")

scrollbar = Scrollbar(messages_frame)

msg_list = Listbox(messages_frame, height = 15, width = 50, yscrollcommand = scrollbar.set)

scrollbar.pack(side = RIGHT, fill = Y)
msg_list.pack(side = LEFT, fill = BOTH)
msg_list.pack()
messages_frame.pack()


entry_box = Entry(window, textvariable = my_msg)
entry_box.bind("<Return>", send)
entry_box.pack()

send_button = Button(window, text = "Send",command = send)
send_button.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()
'''


'''
Mijn lieve chat
'''

from tkinter import *
import csv

def enter_save_name(): 
     name = name_entrybox.get()
     chat_body.insert(END, name + ":")
     name_entrybox.delete(0, END)
     file = open("chat_main.csv", "a")
     newrecord = name + ":"
     file.write(newrecord)
     file.close()


def send_save_msg():
    msg = message_entrybox.get()
    chat_body.insert(END, msg + "\n")
    message_entrybox.delete(0, END)

    file = open("chat_main.csv", "a")
    newrecord = msg + "\n"
    file.write(newrecord)
    file.close()


window = Tk()
window.title("Chat")
window.geometry("500x500")

label_name = Label(text = "Enter your name")
label_name.place (x = 30, y = 30) 

name_entrybox = Entry(text = "")
name_entrybox.place(x = 30, y = 50, width = 100, height = 25)

enter_button = Button(text = "Enter", command = enter_save_name)
enter_button.place(x = 300, y = 50) 

label_msg = Label(text = "Enter your message")
label_msg.place (x = 30, y = 290) 

chat_body = Listbox()
chat_body.place(x = 30, y = 80, width = 300, height = 200)

message_entrybox = Entry(text = "")
message_entrybox.place(x =30, y = 320, width = 300, height = 60)

send_button = Button(text = "Send", command = send_save_msg)
send_button.place(x = 350, y = 320) 


window.mainloop()