from turtle import Turtle
from random import randint
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.turtlesize(0.7,0.7)
        self.set_position()

    def set_position(self):
        print("inside set_position")
        x=randint(-280,280)
        y=randint(-280,280)
        self.goto(x,y)