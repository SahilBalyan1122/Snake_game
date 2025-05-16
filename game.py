
class Game:
    def __init__(self,screen,snake,food,scorecard):
        self.screen = screen
        self.snake = snake
        self.food = food
        self.scorecard = scorecard
        self.Snake_speed = 500
        self.game_over = False

    def setup_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)  # Turns off the screen updates
        self.screen.listen()
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")

    def move(self,delay=True):
        if not self.game_over:
            self.snake.move_tail()
            self.snake.head.forward(20)
            self.screen.update()
            self.check_collisions()
            if delay:
                self.screen.ontimer(self.move, self.Snake_speed)

    def check_collision_with_food(self):
        if self.snake.head.distance(self.food) < 15:
            self.food.set_position()
            self.scorecard.update_score()
            if (not self.scorecard.score%3) and (self.Snake_speed > 50):
                self.Snake_speed -= 50
            self.snake.add_segment(self.snake.body[-1].pos())

    def check_collisions(self):
        self.check_collision_with_food()
        if self.snake.check_collision_with_walls() or self.snake.check_collision_with_tail():
            self.scorecard.game_over()
            self.game_over = True
