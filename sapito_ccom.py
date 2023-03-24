import turtle
import random
import time


# make the log objects
class Log(turtle.Turtle):
   def __init__(self, x, y):
    self.x = x
    self.y = y
    self.turtle = turtle.Turtle()
    self.turtle.penup()
    self.turtle.hideturtle()
    self.turtle.goto(x, y)
    self.turtle.setheading(0)
    self.turtle.pendown()
    self.turtle.fillcolor("brown")
    self.turtle.begin_fill()
    for i in range(2):
        self.turtle.forward(180)
        self.turtle.left(90)
        self.turtle.forward(60)
        self.turtle.left(90)
    self.turtle.end_fill()

    def move(self):
        # the logs will only move from left to right for now
        self.forward(self.speed)

        # if the log start to go off the screen, move it to the other side
        if self.xcor() > screen.window_width() / 2:
            self.goto(-screen.window_width() / 2, self.ycor())
        
        if self.xcor() < -screen.window_width() / 2:
            self.goto(screen.window_width() / 2, self.ycor())




def draw_green_area(x, y):
    green_turtle = turtle.Turtle()
    green_turtle.penup()
    green_turtle._tracer(0)
    green_turtle.goto(x, y)
    green_turtle.begin_fill()
    green_turtle.fillcolor("green")
    green_turtle.setheading(0)
    green_turtle.forward(750)
    green_turtle.setheading(90)
    green_turtle.forward(150)
    green_turtle.setheading(180)
    green_turtle.forward(750)
    green_turtle.setheading(270)
    green_turtle.forward(150)
    green_turtle.end_fill()   

def draw_blue_area(x, y):
    blue_turtle = turtle.Turtle()
    blue_turtle.penup()
    blue_turtle._tracer(0)
    blue_turtle.goto(x, y)
    blue_turtle.begin_fill()
    blue_turtle.fillcolor("blue")
    blue_turtle.setheading(0)
    blue_turtle.forward(750)
    blue_turtle.setheading(90)
    blue_turtle.forward(150)
    blue_turtle.setheading(180)
    blue_turtle.forward(750)
    blue_turtle.setheading(270)
    blue_turtle.forward(150)
    blue_turtle.end_fill()

def draw_grey_area():
    grey_turtle = turtle.Turtle()
    grey_turtle.penup()
    grey_turtle._tracer(0)
    grey_turtle.goto(-375, -75)
    grey_turtle.begin_fill()
    grey_turtle.fillcolor("grey")
    grey_turtle.setheading(0)
    grey_turtle.forward(750)
    grey_turtle.setheading(90)
    grey_turtle.forward(150)
    grey_turtle.setheading(180)
    grey_turtle.forward(750)
    grey_turtle.setheading(270)
    grey_turtle.forward(150)
    grey_turtle.end_fill()


def build_world():

    # Create the screen
    screen = turtle.Screen()
    screen.title("Sapito")
    screen.bgcolor("black")
    screen.setup(width=750, height=750)

    # Draw the green area
    draw_green_area(-375, -375)

    # Draw the blue area
    draw_blue_area(-375, -225)

    # Draw the grey area
    draw_grey_area()

    # Draw the blue area 2
    draw_blue_area(-375, 75)

    # Draw the green area 2
    draw_green_area(-375, 225)


    
    return screen


# # Set up the pause variable
# paused = False

# def pause_game():
#     global paused
#     if not paused:
#         paused = True

#         # hide the turtle and clear its drawings
#         t.hideturtle()
#         t.clear()

#         # write the "Paused" text
#         pen.clear()
#         pen.color("white")
#         pen.write("Paused", align="center", font=("Arial", 50, "normal"))

#         # write the "Press Enter to continue" text
#         pen.penup()
#         pen.goto(0, -75)
#         pen.pendown()
#         pen.write("Press Escape to continue", align="center", font=("Arial", 20, "normal"))

#         # write the "Press Q to quit" text
#         pen.penup()
#         pen.goto(0, -150)
#         pen.pendown()
#         pen.write("Press Q to quit", align="center", font=("Arial", 20, "normal"))

#         # write the "Press R to restart" text
#         pen.penup()
#         pen.goto(0, -225)
#         pen.pendown()
#         pen.write("Press R to restart", align="center", font=("Arial", 20, "normal"))

#     else:
#         paused = False
#         # reset pen position
#         pen.penup()
#         pen.goto(0, 0)


#         # show the turtle and restore its last action
#         t.undo()

#         # clear the "Paused" text
#         pen.clear()

#         # Update the screen
#         screen.update()
#         t.showturtle()

# def quit_game():
#     global paused
#     if paused:
#         screen.bye()
#         # exit the program
#         exit()

# def restart_game():
#     global paused
#     if paused:
#         # reset the turtle position
#         t.penup()
#         t.goto(0, 0)
#         t.pendown()
#         t.setheading(0)

#         # reset the pen position
#         pen.penup()
#         pen.goto(0, 0)
#         pen.pendown()

#         # reset the paused variable
#         paused = False

#         # clear the "Paused" text
#         pen.clear()

#         # Update the screen
#         screen.update()
#         t.showturtle()



# # Listen for key presses
# screen.onkeypress(pause_game, 'Escape')
# screen.onkeypress(quit_game, 'q')
# screen.onkeypress(restart_game, 'r')
# screen.listen()


# spawn the logs
def spawn_logs():
    logs = []
    log1 = Log(-375, -225)
    # logs.append(log1)
    # logs.append(log2)
    # logs.append(log3)
    # logs.append(log4)
    return logs

screen = build_world()

# Main game loop
while True:
    
    spawn_logs()


    # Update the screen
    screen.update()

