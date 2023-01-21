# calling imports
from score import ScoreBoard as SB
from score import HighScoreBoard as HSB
from turtle import Screen
import time
import snake
import food

# creating snake body

# setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake a Snack")
screen.tracer(0)

high_score=HSB()
score = SB()
snake = snake.Snake()
food = food.Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# moving snake
game_on = True
high_score.set_high()
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.score_counter += 1
        if score.score_counter > high_score.high_score_counter:
            high_score.high_score_counter = score.score_counter
            high_score.clear()
            high_score.write(f" High Score: {high_score.high_score_counter}", move=False, align="center", font=('Arial', 16, 'normal'))
        food.refresh()
        score.clear()
        score.write(f"Score: {score.score_counter}", move=False, align="center", font=('Arial', 16, 'normal'))
        snake.extend()

    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reeset()
        with open("data.txt", mode="w") as file:
            file.write(str(high_score.high_score_counter))
        score.score_counter = 0
        score.clear()
        score.write(f"Score: {score.score_counter}", move=False, align="center", font=('Arial', 16, 'normal'))

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.reeset()
            score.score_counter = 0
            with open("data.txt" ,mode="w") as file:
                file.write(str(high_score.high_score_counter))
            score.clear()
            score.write(f"Score: {score.score_counter}", move=False, align="center", font=('Arial', 16, 'normal'))

# close
high_score.temp = high_score.high_score_counter
screen.exitonclick()
