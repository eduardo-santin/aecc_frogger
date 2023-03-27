import turtle
import random
import time


# make the log objects
class Log(turtle.Turtle):
    def __init__(self, x, y, speed):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=3, stretch_len=7)
        self.penup()
        self.goto(x, y)
        self.color("brown")
        self.speed = speed

    def move(self):
        self.goto(self.xcor() - self.speed, self.ycor())
        if self.xcor() < -400:
            self.goto(400, self.ycor())





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


# spawn the logs
def spawn_logs():
    # spawn 2 in both blue areas
    logs_for_area1 = []
    logs_for_area2 = []

    # spawn 2 logs in the first blue area
    # the x could be anywhere between -375 and 180
    x1 = random.randint(-375, 180)
    x2 = random.randint(-375, 180)
    log1 = Log(x1, -190, 2)
    log2 = Log(x2, -110, 1)
    logs_for_area1.append(log1)
    logs_for_area1.append(log2)

    # spawn 2 logs in the second blue area
    # the x could be anywhere between -375 and 180
    x1 = random.randint(-375, 180)
    x2 = random.randint(-375, 180)
    log1 = Log(x1, 110, 2)
    log2 = Log(x2, 190, 1)
    logs_for_area2.append(log1)
    logs_for_area2.append(log2)

    screen.update()
    
    return logs_for_area1, logs_for_area2



screen = build_world()
logs_for_area1, logs_for_area2 = spawn_logs()




# Main game loop
while True:
    for log in logs_for_area1:
        log.move()
    for log in logs_for_area2:
        log.move()
    screen.update()
    time.sleep(0.1)
