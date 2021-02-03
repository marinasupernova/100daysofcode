#from tkinter import *

# window = Tk()
# window.title("Window Title")
# window.geometry("450x100")

# label = Label(text = "Enter a number: ")

# entry_box = Entry (text = 0)

# output_box = Message(text = 0)


# output_box ["bg"] = "red"

# output_box ["fg"] = "white"

# output_box ["relief"] = "sunken"

# list_box = Listbox()

# entry_box ["justify"] = "center"

# button1 = Button(text = "click here", command = click)

# label.place(x = 50, y = 20, width = 100, height = 25)

# entry_box.delete(0, END)

# num = entry_box.get()

# answer = output_txt["text"]

# output_txt["text"] = total

# window.mainloop()
 #widget what is it


# from tkinter import *

# window = Tk()
# window.title("Its my py")
# window.geometry("450x100")

# label = Label(window, text = "Hello world")

# to put things on the window - to make size as it is

# label.pack()

# specifies where text will be placed in the window
# label.place(x = 50, y = 20, width = 100, height = 25)

# entry_box = Entry (text = 0)
# name = entry_box.get()

# window.mainloop()

'''Task 124 '''

#from tkinter import *

# def click():
#     name = textbox1.get()
#     message = str("Hello " + name)
#     textbox2["bg"] = "yellow"
#     textbox2["fg"] = "blue"
#     textbox2["text"] = message

# window = Tk()
# window.geometry("500x200")

# label = Label(text = "What is your name?")
# label.place(x = 30, y = 20)

# textbox1 = Entry(text = "")
# textbox1.place(x = 150, y = 20, width = 200, height = 25)
# textbox1["justify"] = "center"
# textbox1.focus()

# button1 = Button(text = "Press me", command = click)
# button1.place(x = 30, y = 50, width = 120, height = 25)


# textbox2 = Message(text = "")
# textbox2.place(x = 150, y = 50, width = 200, height = 25)
# textbox2["bg"] = "white"
# textbox2["fg"] = "black"



# window.mainloop()

'''Task 125 

from tkinter import *
import random

def rand_num():
    random_number = str(random.randint(1, 6))
    textbox["text"] = str(random_number)


window = Tk()
window.title ("Roll a dice")
window.geometry("500x200")

button = Button(text = "Roll", command = rand_num)
button.place(x = 30, y = 50, width = 120, height = 25)

textbox = Message(text = "")
textbox.place(x = 150, y = 50, width = 50, height = 25)
textbox["bg"] = "white"
textbox["fg"] =  "black"

window.mainloop() '''

'''Task 128'''


# from tkinter import *


# def do_onclick():
#     km = textbox1.get()
#     message = convert_km_to_ml(int(km))
#     textbox2["text"] = str(message) + " miles"

# def convert_km_to_ml(km): 
#     ml= km * 0.6214
#     return ml


# window = Tk()
# window.title("Converter")
# window.geometry("500x200")

# label = Label(text = "Enter the the distance in km")
# label.place(x = 30, y = 20)

# textbox1 = Entry(text = "")
# textbox1.place(x = 210, y = 20, width = 150, height = 25)
# textbox1["justify"] = "center"
# textbox1.focus()

# button1 = Button(text = "Convert into miles", command = do_onclick)
# button1.place(x = 30, y = 50, width = 120, height = 25)

# textbox2 = Message(text = "")
# textbox2.place(x = 150, y = 50, width = 150, height = 25)
# textbox2["bg"] = "white"
# textbox2["fg"] =  "black"

# window.mainloop()



'''Task 126 

1. enter a number in the box

2. add that number to a total on click 

3. display total in another box 

4. create button that resets total back to 0 and empty the oroginal box'''

'''
from tkinter import *

def add_to_total(): 
    num = int(textbox_enter.get())
    total = 0
    total = total + num
    textbox_total["text"] = str(total)

def reset():
    textbox_total["text"] = 0 #?
    textbox_enter.delete(0, END) #?
    textbox_enter.focus()



window = Tk()
window.geometry("500x500")

label_enter = Label(text = "Enter a number: ")
label_enter.place(x = 30, y = 20)

textbox_enter = Entry(text = "")
textbox_enter.place(x = 150, y = 20, width = 50, height = 25)

button_add = Button(text = "Add ", command = add_to_total)
button_add.place(x = 230, y = 20)

label_total = Label(text = "Result: ")
label_total.place(x = 30, y = 50)

textbox_total = Message(text = "")
textbox_total.place(x = 150, y = 50, width = 50, height = 25)
textbox_total["bg"] = "white"
textbox_total["relief"] = "sunken"

button_reset = Button(text = "Reset", command = reset)
button_reset.place(x = 230, y = 50)

window.mainloop()
'''

'''Task 127
1. enter a name in a text box
2. add on click to the list displayed on the screen
3. clear the list on click 
'''


from tkinter import *

def add_on_click():
    name = name_entry.get()
    # name_list = []
    # name_list.append(name)
    # output_list["text"] = my_list
    name_list.insert(END, name)
    name_entry.delete(0, END)
    name_entry.focus()


    


def clear():
    name_list.delete(0, END)
    name_entry.focus()



window = Tk()
window.title("What's your name? ")
window.geometry("500x500")

label = Label(text = "Please enter your name: ")
label.place(x = 30, y = 20)

name_entry = Entry(text = "")
name_entry.place(x = 180, y = 20, width = 150, height = 25)

button_add = Button(text = "Add to the list", command = add_on_click)
button_add.place(x = 30, y = 50)

name_list = Listbox()
name_list.place(x = 180, y = 50, width = 150, height = 60)

button_clear = Button(text = "Clear the list",command = clear)
button_clear.place(x = 350, y = 50)


window.mainloop()