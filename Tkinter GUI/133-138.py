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

window.wm_iconbitmap("/Users/marina/workspace/100daysofcode/Tkinter GUI/girl.ico")

window.configure(background = "light green")

logo = PhotoImage(file = "/Users/marina/workspace/100daysofcode/Tkinter GUI/the_cat.gif")
logoimage = Label(image = logo)
logoimage.place(x = 30, y = 20, width = 200, height = 200)

photo = PhotoImage(file = "/Users/marina/workspace/100daysofcode/Tkinter GUI/the_cat.gif" )
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



