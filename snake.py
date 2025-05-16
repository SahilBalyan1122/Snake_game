from turtle import Turtle


class Snake:
    
    def __init__(self):
        self.body = []
        self.make_snake()
        self.head = self.body[0]
        self.game = None

    def make_snake(self):
        for i in range(3):
            self.add_segment((-20*i,0))

    def add_segment(self,pos):
        self.body.append(Turtle("square"))
        self.body[-1].color("white")
        self.body[-1].penup()
        self.body[-1].goto(pos)
        self.body[-1].speed("slowest")

    def move_tail(self):
        length = len(self.body)
        for i in range(length-1,0,-1):
            self.body[i].setpos(self.body[i-1].pos())


    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)
            self.game.move(False)
    

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
            self.game.move(False)


    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)
            self.game.move(False)



    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)
            self.game.move(False)



    def check_collision_with_walls(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        return False

    def check_collision_with_tail(self):
        for segment in self.body[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False