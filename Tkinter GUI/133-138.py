
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

from tkinter import *

def add_to_listbox():

    name = enter_name.get()
    enter_name.delete(0, END)
    
    gender = select_gender.get()
    select_gender.set("Select gender")

    new_data = name + "," + gender + "\n"
    names_list.insert(END, new_data)
    enter_name.focus()



window = Tk()
window.title("Name + gender")
window.geometry("500x500")

label_name = Label(text = "Enter a name: ")
label_name.place(x = 30, y = 20, width = 100, height = 25)

enter_name = Entry(text = "")
enter_name.place (x = 150, y = 20, width = 100, height = 25)

select_gender = StringVar(window)
select_gender.set("Select gender")

gender_list = OptionMenu(window, select_gender, "Man", "Woman", "Other")
gender_list.place(x = 30, y = 70)


button_add = Button(text = "Add", command = add_to_listbox)
button_add.place(x = 175, y = 70)


names_list = Listbox()
names_list.place(x = 30, y = 120, width = 130, height = 80)



window.mainloop()


