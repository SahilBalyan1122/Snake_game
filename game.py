# from main import reload
import time

class Game:
    def __init__(self,screen,snake,food,scorecard, reload):
        self.screen = screen
        self.snake = snake
        self.food = food
        self.scorecard = scorecard
        self.reload = reload
        self.Snake_speed = 500
        self.game_over = False
        self.pause = False
        self.moved = time.time()*1000 + self.Snake_speed  # Initialize moved with current time in milliseconds

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

    def move(self,turn=False):
        # print(f"Moving -{self.run}")
        if not turn and time.time()*1000 < self.moved + self.Snake_speed:
            print(f"{time.time()*1000} - {self.moved + self.Snake_speed}")
            return
        if not self.game_over:
            self.moved = time.time()*1000
            self.snake.move_tail()
            self.snake.head.forward(20)
            self.screen.update()
            self.check_collisions()
            self.screen.ontimer(self.move, int(self.Snake_speed))

    def check_collision_with_food(self):
        if self.snake.head.distance(self.food) < 15:
            self.food.set_position()
            self.scorecard.update_score()
            if (not self.scorecard.score%3):
                self.Snake_speed *= .9
            self.snake.add_segment(self.snake.body[-1].pos())

    def check_collisions(self):
        self.check_collision_with_food()
        if self.snake.check_collision_with_walls() or self.snake.check_collision_with_tail():
            self.scorecard.game_over()
            self.game_over = True

    def pause_game(self):
            self.game_over = True
            self.screen.onkey(self.reload, "r")
            self.scorecard.show_text("Game Paused. Press 'r' to reload and 'c' to continue.")

    def unpause_game(self):
            self.game_over = False
            self.screen.onkey(None, "r")
            self.move()