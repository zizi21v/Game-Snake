from turtle import  Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

 #creacion del tablero de el juego
screen = Screen ()
screen.setup(width=600, height=600)
screen.bgcolor("pink")
screen.title("Snake game")
screen.tracer (0)
snake = Snake()
food = Food()
#Creamos el objeto tablero
scoreboard = ScoreBoard()


#metodo que escucha las teclas
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
  
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280  or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()
    
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()