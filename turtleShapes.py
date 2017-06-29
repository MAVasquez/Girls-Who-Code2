from turtle import *
import math

# Name your Turtle.
#t = Turtle()

# Set Up your screen and starting position.
setup(600,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
def drawShape(turtle,sides, color):
    turtle.pencolor(color)
    drawnSides = 0
    angle =360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.right(angle)
        drawnSides+=1
        
##########################################

#RUNNING PROGRAM
another = True

mar = Turtle()
mar.pencolor("blue")
mar.turtlesize(2,2)
mar.pensize(10)
mar.pendown()

while another == True:
    print("how many sides do you want your shape to have?")
    numSides = int(input())
    
    print("what color do you want your shape to have?")
    chosenColor = input()

    drawShape(mar, numSides, chosenColor)

    print("do you want to draw another shape?")
    answer = input()
    if (answer == "no"):
        another = False

# Close window on click.
exitonclick()

