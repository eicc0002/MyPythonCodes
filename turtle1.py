import turtle
import random

# Settings
turtle.shape("turtle")
turtle.speed("fastest")
turtle.Screen().colormode(255)

numRows = int(input("Enter number of rows: "))
numColumns = int(input("Enter number of columns: "))
radius = 50
startPos_x = -350
startPos_y = 300

turtle.penup()
turtle.goto(startPos_x, startPos_y)
turtle.pendown()

for i in range(numRows):
    # Draw 1 Row
    for j in range(numColumns):
        # Draw and fill a circle
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.color(r, g, b)
        turtle.begin_fill()
        turtle.circle(radius, 360)
        turtle.end_fill()

        # Move to a new position
        turtle.penup()
        turtle.forward(radius * 2)
        turtle.pendown()

    # Move to next row
    startPos_y = startPos_y - (radius * 2)
    turtle.penup()
    turtle.goto(startPos_x, startPos_y)
    turtle.pendown()


turtle.mainloop()

