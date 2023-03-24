import turtle
import random


# make the log objects
class Log(turtle.Turtle):
    def __init__(self, x, y, width, height, color, speed):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=height, stretch_len=width)
        self.goto(x, y)
        self.speed = speed

    def move(self):
        # the logs will only move from left to right for now
        self.forward(self.speed)

        # if the log start to go off the screen, move it to the other side
        if self.xcor() > screen.window_width() / 2:
            self.goto(-screen.window_width() / 2, self.ycor())
        
        if self.xcor() < -screen.window_width() / 2:
            self.goto(screen.window_width() / 2, self.ycor())
        
        

# Create pen turtle to write on the screen
pen = turtle.Turtle()
pen.hideturtle()


# Set up the pause variable
paused = False

def pause_game():
    global paused
    if not paused:
        paused = True

        # hide the turtle and clear its drawings
        t.hideturtle()
        t.clear()

        # write the "Paused" text
        pen.clear()
        pen.color("white")
        pen.write("Paused", align="center", font=("Arial", 50, "normal"))

        # write the "Press Enter to continue" text
        pen.penup()
        pen.goto(0, -75)
        pen.pendown()
        pen.write("Press Escape to continue", align="center", font=("Arial", 20, "normal"))

        # write the "Press Q to quit" text
        pen.penup()
        pen.goto(0, -150)
        pen.pendown()
        pen.write("Press Q to quit", align="center", font=("Arial", 20, "normal"))

        # write the "Press R to restart" text
        pen.penup()
        pen.goto(0, -225)
        pen.pendown()
        pen.write("Press R to restart", align="center", font=("Arial", 20, "normal"))

    else:
        paused = False
        # reset pen position
        pen.penup()
        pen.goto(0, 0)


        # show the turtle and restore its last action
        t.undo()

        # clear the "Paused" text
        pen.clear()

        # Update the screen
        screen.update()
        t.showturtle()

def quit_game():
    global paused
    if paused:
        screen.bye()
        # exit the program
        exit()

def restart_game():
    global paused
    if paused:
        # reset the turtle position
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(0)

        # reset the pen position
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()

        # reset the paused variable
        paused = False

        # clear the "Paused" text
        pen.clear()

        # Update the screen
        screen.update()
        t.showturtle()

def build_world():

    # set up the screen 
    # the width and height of the screen are ful

    screen = turtle.Screen()
    screenTK = screen.getcanvas().winfo_toplevel()
    screenTK.attributes("-fullscreen", True)
    screen.bgcolor("black")
    # make window border be 0
    screenTK.overrideredirect(1)
    screenTK.update()


    # paint the top of the screen up to 1/8th of the height
    final_area = turtle.Turtle()
    # turn off turtle animation and set delay to 0
    final_area.hideturtle()
    final_area._tracer(0)
    final_area.getscreen().delay(0)

    final_area.penup()
    final_area.goto(-screen.window_width()/2, screen.window_height() / 2)
    final_area.pendown()
    final_area.begin_fill()
    final_area.fillcolor("green")
    final_area.forward(screen.window_width())
    final_area.right(90)

    height = screen.window_height() / 8
    final_area.forward(height)
    final_area.right(90)
    final_area.forward(screen.window_width())
    final_area.end_fill()

    
    road_area2 = turtle.Turtle()
    road_area2.shape("square")
    road_area2.hideturtle()
    road_area2._tracer(0)
    road_area2.getscreen().delay(0)



    road_area2.penup()
    starting_point = screen.window_height() / 2 - height
    road_area2.goto(-screen.window_width()/2, starting_point)
    road_area2.pendown()
    road_area2.begin_fill()
    road_area2.fillcolor("gray")
    road_area2.forward(screen.window_width())
    road_area2.right(90)
    height = height * 2
    road_area2.forward(height)
    road_area2.right(90)
    road_area2.forward(screen.window_width())
    road_area2.end_fill()

    river_area = turtle.Turtle()
    river_area.shape("square")
    river_area.hideturtle()
    river_area._tracer(0)
    river_area.getscreen().delay(0)

    river_area.penup()
    starting_point = starting_point - height
    river_area.goto(-screen.window_width()/2, starting_point)
    river_area.pendown()
    river_area.begin_fill()
    river_area.fillcolor("blue")
    river_area.forward(screen.window_width())
    river_area.right(90)
    height = height 
    river_area.forward(height)
    river_area.right(90)
    river_area.forward(screen.window_width())
    river_area.end_fill()

    road_area = turtle.Turtle()
    road_area.shape("square")
    road_area.hideturtle()
    road_area._tracer(0)
    road_area.getscreen().delay(0)
    
    road_area.penup()
    starting_point = starting_point - height
    road_area.goto(-screen.window_width()/2, starting_point)
    road_area.pendown()
    road_area.begin_fill()
    road_area.fillcolor("gray")
    road_area.forward(screen.window_width())
    road_area.right(90)
    height = height
    road_area.forward(height)
    road_area.right(90)
    road_area.forward(screen.window_width())
    road_area.end_fill()

    # paint the bottom of the screen up to 1/8th of the height
    starting_area = turtle.Turtle()
    starting_area.shape("square")
    starting_area.hideturtle()
    starting_area._tracer(0)
    starting_area.getscreen().delay(0)

    starting_area.penup()
    starting_point = starting_point - height
    starting_area.goto(-screen.window_width()/2, starting_point)
    starting_area.pendown()
    starting_area.begin_fill()
    starting_area.fillcolor("green")
    starting_area.forward(screen.window_width())
    starting_area.right(90)
    height = height
    starting_area.forward(height)
    starting_area.right(90)
    starting_area.forward(screen.window_width())
    starting_area.end_fill()
    





    return screen




screen = build_world()

# Listen for key presses
screen.onkeypress(pause_game, 'Escape')
screen.onkeypress(quit_game, 'q')
screen.onkeypress(restart_game, 'r')
screen.listen()


# Main game loop
while True:
    # create world
    # build_world()


    if not paused:
        # Move the turtle forward
        t.forward(10)

        # Check if the turtle has hit the edge of the screen
        if t.xcor() > 200 or t.xcor() < -200 or t.ycor() > 200 or t.ycor() < -200:
            # Turn the turtle around
            t.left(180)

    # Update the screen
    screen.update()

