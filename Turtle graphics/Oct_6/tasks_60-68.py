import turtle

'''Task 60
pen = turtle.Turtle()
for i in range (4):
    pen.forward(300)
    pen.left(90)

turtle.exitonclick()'''

'''Task 61
pen = turtle.Turtle()
for i in range (3):
    pen.forward(200)
    pen.left(120)'''

'''Task 62
pen = turtle.Turtle()
pen.circle(100)'''

'''Example for nested loops
pen = turtle.Turtle()
for i in range (0, 10):
    pen.right(36)
    for i in range (0, 5):
        pen.forward(100)
        pen.right(72)'''


'''Task 63
turtle.begin_fill()
turtle.color("red")
for i in range (4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.forward(150)
turtle.pendown()

turtle.begin_fill()
turtle.color("blue")
for i in range (4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.forward(150)
turtle.pendown()

turtle.begin_fill()
turtle.color("yellow")
for i in range (4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()'''

'''Task 63 a try with loops
colors = ["blue", "orange", "red"]
for i in range (0, 3):
    turtle.color(colors[i])
    turtle.begin_fill()
    
    for i in range (4):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(150)
        turtle.penup()
    
    
    turtle.end_fill()'''

'''Task 64
for i in range (5):
    
    turtle.forward(100)
    turtle.left(144)'''

'''Task 65'''    
'''1
turtle.left (90)
turtle.forward(100)
turtle.back(100)

turtle.penup()
turtle.right(90)
turtle.forward(150)
turtle.pendown()

2
turtle.forward(100)
turtle.back(100)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.pendown()

3

turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.back(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)'''

'''Task 66
import random
colors = ["blue", "orange", "red", "yellow", "indigo", "white", "purple", "black"]
for i in range (0, 8):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.left(45)'''

'''Task 67
for i in range (0, 10):
    turtle.right(36)
    for i in range (0, 8):
        turtle.forward(100)
        turtle.left(45)

turtle.hideturtle()
turtle.exitonclick() '''

'''Task 68
import random
lines = random.randint(10, 30)

for i in range (0, lines):
    length = random.randint(50, 200)
    angle = random.randint(15, 180)
    turtle.forward(length)
    turtle.right(angle)

turtle.exitonclick()'''

'''def greet():
    print("Hello, person!")'''

'''def greet (name):
    print("Hello, person!")

def greet (name):
    print(f"Hello, {name}!")

greet("Marina")'''
'''
def greet(name, is_new):
    if(is_new):
        print(f"Hello, {name}! Nice to meet you!")
    else:
        print(f"What's up, {name}? Nice to see you again!")

greet("Marina", False)
greet("Carla", True)
greet("Bernard", False)
greet("Duke", True)'''

'''Superpower
def superpower(name, power):
     print(f"Hi, I'm {name} and my superpower is {power}")

superpower("Marina", "Python")'''

'''Funny Greeting
def funny_greeting (color, dessert):
    print(f"My favorite dessert is {color} because it tastes so good, and my favorite color is {dessert} because it is very pretty!!")

funny_greeting("violet", "cheesecake")'''



