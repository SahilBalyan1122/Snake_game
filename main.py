from turtle import Screen
from snake import Snake
from scorecard import ScoreCard
from food import Food
from game import Game
import time
# run=1


def reload():
    global run
    # run+=1
    screen = Screen()
    print("Reloading...screen")
    screen.clear()
    snake = Snake()
    scorecard = ScoreCard()
    food = Food()
    game = Game(screen,snake,food,scorecard,reload)
    game.setup_screen()
    # game.run = run
    snake.game = game
    game.move(True)
    screen.onkey(game.pause_game, "p")
    screen.onkey(game.unpause_game, "c")
    screen.exitonclick()


reload()


