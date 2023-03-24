from turtle import Turtle, Screen, _Screen

screen_offset = 80
class Player(Turtle):
    def __init__(self, screen:_Screen ,color):
        
        screen.addshape("frog_up", 
        
                        ((10,0),(6,0),(6,4),(4,6),(4,8),(2,8),(2,6),(-2,6),(-2,8),(-4,8),(-4,6),(-6,4),(-6,0) ,(-10,0),(-10,-4), (10,-4)))
        screen.addshape('frog_right',
                        ((10,0),(6,0),(6,8),(2,8),(2,6),(-10,0),(-10,-4),(10,-4)))
        screen.addshape('frog_left',
                        ((-10,0),(-6,0),(-6,8),(-2,8),(-2,6),(10,0),(10,-4),(-10,-4)))
        Turtle.__init__(self,shape="frog_up")

        self.color("black",color)
        self.begin_fill()
        self.shape("frog_up")
        self.end_fill()
        self.shapesize(4,4,4)
        self.setheading(90)
        self.settiltangle(0)
        self.penup()
        self.setpos(0,-360)

    def up(self):
        self.shape('frog_up')
        if self.heading() != 90:
           
            self.setheading(90)
            self.settiltangle(0)
            
        
        if(self.position()[1] <= (self.screen.window_height()/2)-screen_offset):
            self.forward(60)
        #self.sword.turt.forward(60)
        #self.sword.move(90,0, self.turt.pos())

        
    
    def down(self):
        self.shape('frog_up')
        if self.heading() != 270:
            
            self.setheading(270)
            self.settiltangle(0)
            
        
        if(self.position()[1] >= -1*(self.screen.window_height()/2-screen_offset)):
            self.forward(60)


        
        
    
    def left(self):
        self.shape('frog_left')
        if self.heading() != 180:
            #self.turt.setheading(180)
            self.setheading(180)
            self.settiltangle(270)

            
        
        if(self.position()[0] >= -1*(self.screen.window_height()/2 -screen_offset)):
            self.forward(60)


        

    
    def right(self):
        self.shape('frog_right')
        if self.heading() != 0:
            
            self.setheading(0)
            self.settiltangle(90)
            
        if(self.position()[0] <= (self.screen.window_height()/2)-screen_offset):
            self.forward(60)
        #self.sword.turt.forward(60)
        #self.sword.move(0,0, self.turt.pos())
        #if(self.turt.position()[0] != screen.window_height/2):
       
        #self.turt.forward(60)
         
        
    
        
