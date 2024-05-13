#This is the ball for the very simple Breakout game

from turtle import Turtle

MOVE_DIST = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move_dist = MOVE_DIST
        self.y_move_dist = MOVE_DIST
        self.reset()

    def move(self):
        #Move only 10 steps ahead, both vertically
        #and horizontally.
        new_y = self.ycor() + self.y_move_dist
        new_x = self.xcor() + self.x_move_dist
        self.goto(x=new_x, y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            #Reverse the horizontal direction
            self.x_move_dist *= -1

        if y_bounce:
            #Reverse the vertical direction
            self.y_move_dist *= -1

    def reset(self):
        #Ball should got to an initial position,
        #always moving up.
        self.goto(x=0, y=-240)
        self.y_move_dist = 10