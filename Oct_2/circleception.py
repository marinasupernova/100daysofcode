import turtle
'''circle_orange = turtle.Turtle()
circle_orange.fillcolor('orange')
circle_orange.begin_fill()
circle_orange.circle(100)
circle_orange.end_fill()

circle_blue = turtle.Turtle()
circle_blue.fillcolor('blue')
circle_blue.begin_fill()
circle_blue.circle(50)
circle_blue.end_fill()

circle_white = turtle.Turtle()
circle_white.fillcolor('white')
circle_white.begin_fill()
circle_white.circle(25)
circle_white.end_fill()'''


radius = 100

# colors = ['blue', 'orange', 'white']
color = 'black' 

for i in range (0, 3):
    mycircle = turtle.Turtle()
    if radius == 100:
        color = 'blue' 
    if radius == 75:
        color = 'orange' 
    if radius == 50:
        color = 'white'         
    # mycircle.fillcolor(colors[i])
    mycircle.fillcolor(color)
    mycircle.begin_fill()
    mycircle.circle(radius)
    mycircle.end_fill()
    radius = radius - 25





turtle.exitonclick()