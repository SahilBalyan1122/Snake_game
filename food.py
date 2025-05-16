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
        x=randint(-14,14)
        y=randint(-14,14)
        self.goto(x*20,y*20)