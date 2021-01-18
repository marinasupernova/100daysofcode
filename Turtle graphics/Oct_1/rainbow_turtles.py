
import turtle
my_turtle = turtle.Turtle()
my_turtle.turtlesize(2, 2, 2)
my_turtle.shape('turtle')
my_turtle.penup()

for i in range (0, 7):
    my_turtle.forward(50)
    if i == 0:
        my_turtle.color('red')
    elif i == 1:
        my_turtle.color('orange')
    elif i == 2:
        my_turtle.color('yellow')
    elif i == 3:
        my_turtle.color('green')
    elif i == 4:
        my_turtle.color('blue')
    elif i == 5:
        my_turtle.color('indigo')
    elif i == 6:
        my_turtle.color('violet')
    my_turtle.stamp()
turtle.exitonclick()
