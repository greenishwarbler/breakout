from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=0.5, stretch_len=2)


class BlockOfBricks:

    def __init__(self):
        self.bricks =[]

    def generate_blocks_of_bricks(self, COLORS_BRICKS,
                                  x_starting_position_brick, y_starting_position_brick,
                                  x_shift, y_shift):
        '''generates all 8 blocks of bricks \n
            COLORS_BRICKS - list of colors for every block, one color for one row \n
            x_starting_position_brick - starting x coordinate of lower left corner \n
            y_starting_position_brick - starting y coordinate of lower left corner \n
            x_shift - horizontal spacing between brick centers \n
            y_shift - vertical spacing between brick centers \n'''
        for color in COLORS_BRICKS:
            x_current_position_brick = x_starting_position_brick
            y_current_position_brick = y_starting_position_brick
            for row in range(15):
                brick = Brick(color, (x_current_position_brick, y_current_position_brick))
                brick.x_position = x_current_position_brick
                brick.y_position = y_current_position_brick
                self.bricks.append(brick)
                x_current_position_brick += x_shift
            y_starting_position_brick += y_shift


