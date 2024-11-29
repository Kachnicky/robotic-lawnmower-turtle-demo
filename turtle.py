import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgpic("./bitmap.png")

# Register the turtle shape
screen.register_shape("./tt.gif")

time.sleep(5)
# Create a turtle with the registered shape
t = turtle.Turtle()
t.hideturtle()
t.shape("/.tt.gif")  # Set the turtle shape to the PNG image

t.speed(4)  # Set the speed of the turtle
t.left(90)
t.pensize(10)
t.pencolor("white")

tt = turtle.Turtle()
tt.shape("./tt.gif")  # Set the turt+le shape to the PNG image
tt.hideturtle()

tt.speed(4)  # Set the speed of the turtle
tt.right(90)
tt.pensize(10)
tt.pencolor("white")

# Function to draw the zigzag pattern
def draw_zigzag():



    t.right(90)
    t.penup()
    tt.penup()
    t.goto(-300,300)
    tt.goto(-300,300)
    t.pendown()
    tt.pendown()
    t.showturtle()
    tt.showturtle()
    time.sleep(1)

    tt.forward(300)
    tt.left(90)
    tt.forward(30)

    for j in range(2):  # Number of zigzag lines
        # Move to the right edge
        for i in range(5):
            t.forward(30)
            t.right(90)
            tt.right(90)
            tt.forward(300)
            t.forward(300)
            t.left(90)
            tt.left(90)
            t.forward(30)
            tt.forward(30)
            if j == 1 and i == 3:
                tt.left(90)
                tt.forward(150)
                tt.right(90)
                tt.forward(30)
                t.left(90)
                tt.left(90)
                tt.forward(30)
                tt.left(90)
                tt.forward(30)
                tt.right(90)
                t.forward(300)
                tt.forward(120)
                tt.right(90)
                t.right(90)

            else:
                t.left(90)
                tt.left(90)
                t.forward(300)
                tt.forward(300)
                t.right(90)
                tt.right(90)
            if j != 1 or i != 4:
                tt.forward(30)

    t.backward(600)
    tt.backward(600)
    tt.left(90)
    tt.forward(300)
# Start drawing the zigzag pattern
draw_zigzag()

# Hide the turtle and finish
turtle.done()
