from turtle import Screen
from snake import Snake
from scorecard import ScoreCard
from food import Food
from game import Game

screen = Screen()
snake = Snake()
scorecard = ScoreCard()
food = Food()
game = Game(screen,snake,food,scorecard)
game.setup_screen()
snake.game = game
game.move()

screen.exitonclick()
