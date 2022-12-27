import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import BlockOfBricks
block = BlockOfBricks()


# CONSTANTS
SCREEN_WIDTH = 645
SCREEN_HEIGHT = 800
PADDLE_POSITION = (0, -300)
SPACE_BETWEEN_BRICKS = 5
COLORS_BRICKS = ["yellow", "yellow", "green", "green", "orange", "orange", "red", "red"]

# Screen properties
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# Generating scoreboard
scoreboard = Scoreboard()

# Generating blocks of bricks
block.generate_blocks_of_bricks(COLORS_BRICKS, -342.5, 200, 45, 15)

# Generating paddle and ball
paddle = Paddle(PADDLE_POSITION)
ball = Ball()

# start move ball
ball.move()
ball.bounce_y()

# Assigning buttons to move paddle
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")


# game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top wall
    if ball.ycor() > 380:
        ball.bounce_y()
        paddle.shrink_paddle()

    # Detect collision with side walls
    if ball.xcor() > 302.5 or ball.xcor() < -302.5:
        ball.bounce_x()

    # Detect collision with paddle
    delta_y_ball_paddle = ball.ycor() - paddle.ycor()
    delta_x_ball_paddle = ball.xcor() - paddle.xcor()

    ball.hit_paddle(paddle.shapesize()[1], paddle, delta_x_ball_paddle, delta_y_ball_paddle)


    # Detect collision with  bricks
    for brick in block.bricks:
        hits = 0
        delta_y_ball_brick = brick.ycor() - ball.ycor()
        if ball.distance(brick) < 22.4 and (delta_y_ball_brick >= -10 or delta_y_ball_brick <= 10):
            if ball.ycor() > brick.ycor():
                ball.y_move = abs(ball.y_move)
                brick.goto(brick.xcor() * 10, brick.ycor() * 10)
                scoreboard.score_up(brick.color()[0])
                hits += 1
            elif ball.ycor() < brick.ycor():
                ball.y_move = -abs(ball.y_move)
                brick.goto(brick.xcor() * 10, brick.ycor() * 10)
                scoreboard.score_up(brick.color()[0])
                hits += 1
            elif ball.ycor() == brick.ycor():
                ball.y_move = ball.y_move
            if hits % 4 == 0 or brick.color()[0] == "orange" or brick.color()[0] == "red":
                ball.update_speed()

    #Losing life
    if ball.ycor() < -390:
        ball.reset_position()
        scoreboard.lose_life()

    if scoreboard.life == 4:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
