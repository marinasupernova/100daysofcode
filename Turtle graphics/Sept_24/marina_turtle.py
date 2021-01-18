import turtle 
'''turtle.shape('turtle')
turtle.setup(500, 500)
turtle.Screen().bgcolor("blue")
turtle.Screen().colormode(255)
turtle.Screen().bgcolor(29, 162, 216)
turtle.shape('turtle')(9, 185, 13)
turtle.pencolor(0, 128, 0)'''

import random
stamp = turtle.Turtle()
stamp.shape('turtle')
stamp.penup()
turtle.colormode(255)
paces = 20
random_red = 50
random_blue = 50
random_green = 50
for i in range(0, 50):
    random_red = random.randint(0, 255)
    random_blue = random.randint(0, 255)
    random_green = random.randint(0, 255)
    stamp.color(random_red, random_green, random_blue)
    stamp.stamp()
    paces += 3
    stamp.forward(paces)
    stamp.right(25)

pen = turtle.Turtle()
pen.write("Turtles rock!")

Functions: 
turtle.shape('turtle')
turtle.forward() - pixels
turtle.back()
turtle.left() - degrees
turtle.right()

turtle.color("blue")


Doodles and shapes
pen = turtle.Turtle() - we create an instance of turtle object and call it pen
pen = turtle.Turtle()
pen.write("Turtles rock!", font =("Open Sans", 60, "normal"))