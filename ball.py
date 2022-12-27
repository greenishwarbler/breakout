from turtle import Turtle

MOVE_SPEED = 0.04

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 8
        self.y_move = 10
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = MOVE_SPEED

    def update_speed(self):
        self.move_speed *= 0.8

    def hit_paddle(self, paddle_size, paddle, delta_x_ball_paddle, delta_y_ball_paddle):
        """
        bouncing the ball
        :param paddle_size: stretch_len of paddle
        :param paddle: paddle
        :param delta_x_ball_paddle: delta position x ball and paddle
        :param delta_y_ball_paddle: delta position y ball and paddle
        :return:
        """
        # Detect collision with paddle without shrinked paddle
        # Top paddle
        if paddle_size == 2:
            if self.distance(paddle) < 22.4 and delta_y_ball_paddle == 10:
                if (delta_x_ball_paddle <= 19) and (delta_x_ball_paddle >= -19):
                    self.bounce_y()
                elif (delta_x_ball_paddle <= 20) and (delta_x_ball_paddle > 19):
                    self.x_move = abs(self.x_move)
                    self.y_move = abs(self.y_move)
                elif (delta_x_ball_paddle >= -20) and (delta_x_ball_paddle <= -19):
                    self.x_move = -abs(self.x_move)
                    self.y_move = abs(self.y_move)
            # Sides paddle
            elif self.distance(paddle) < 25.5 and delta_y_ball_paddle < 10:
                # Right side paddle
                if delta_x_ball_paddle > 20 and delta_x_ball_paddle <= 25:
                    self.x_move = abs(self.x_move)
                # Left side paddle
                elif delta_x_ball_paddle >= -25 and delta_x_ball_paddle < -20:
                    self.x_move = -abs(self.x_move)

        elif paddle_size == 1:
            if self.distance(paddle) < 14.2 and delta_y_ball_paddle == 10:
                if (delta_x_ball_paddle <= 9) and (delta_x_ball_paddle >= -9):
                    self.bounce_y()
                elif (delta_x_ball_paddle <= 10) and (delta_x_ball_paddle > 9):
                    self.x_move = abs(self.x_move)
                    self.y_move = abs(self.y_move)
                elif (delta_x_ball_paddle >= -10) and (delta_x_ball_paddle <= -9):
                    self.x_move = -abs(self.x_move)
                    self.y_move = abs(self.y_move)
            # Sides paddle
            elif self.distance(paddle) < 16 and delta_y_ball_paddle < 10:
                # Right side paddle
                if delta_x_ball_paddle > 10 and delta_x_ball_paddle <= 15:
                    self.x_move = abs(self.x_move)
                # Left side paddle
                elif delta_x_ball_paddle >= -15 and delta_x_ball_paddle < -10:
                    self.x_move = -abs(self.x_move)