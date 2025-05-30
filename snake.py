from turtle import Turtle,Shape,register_shape

class Snake:
    
    def __init__(self):
        self.make_shape()
        self.body = []
        self.make_snake()
        self.head = self.body[0]
        self.game = None

    def make_shape(self):
        x=1
        gap=3
        s1 = Shape("compound")
        s2 = Shape("compound")
        poly1 = ((13*x,7*x),(0,16*x),(-13*x,7*x),(-13*x,-7*x),(-7*x,-13*x),(7*x,-13*x),(13*x,-7*x))
        poly2 = (((10+gap)*x,(10-gap)*x),((10-gap)*x,(10+gap)*x),((-10+gap)*x,(10+gap)*x),((-10-gap)*x,(10-gap)*x),((-10-gap)*x,(-10+gap)*x),((-10+gap)*x,(-10-gap)*x),((10-gap)*x,(-10-gap)*x),((10+gap)*x,(-10+gap)*x))
        s1.addcomponent(poly1, "yellow", "black")
        s2.addcomponent(poly2, "yellow", "green")
        register_shape("head",s1)
        register_shape("body",s2)

    def make_snake(self):
        for i in range(3):
            self.add_segment((-20*i,0))

    def add_segment(self,pos):
        self.body.append(Turtle("body"))
        self.body[-1].color("white")
        self.body[-1].penup()
        self.body[-1].goto(pos)
        self.body[-1].speed("slowest")
        self.body[-1].shapesize(1,1,3)

    def move_tail(self):
        length = len(self.body)
        for i in range(length-1,0,-1):
            self.body[i].setpos(self.body[i-1].pos())


    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)
            # self.game.move(False)
            self.game.move(True)
    

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
            # self.game.move(False)
            self.game.move(True)


    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)
            self.game.move(True)
            # self.game.move(False)



    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)
            self.game.move(True)
            # self.game.move(False)



    def check_collision_with_walls(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        return False

    def check_collision_with_tail(self):
        for segment in self.body[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False