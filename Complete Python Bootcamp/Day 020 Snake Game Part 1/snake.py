from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.segments = [Turtle(shape="square"), Turtle(shape="square"), Turtle(shape="square")]
        x, y = 10, 10
        for segment in self.segments:
            segment.penup()
            segment.teleport(x, y)
            segment.color("white")
            x -= 20

    def move(self):
        for i in range(0, len(self.segments))[::-1]:
            if i > 0:
                x_cor = self.segments[i - 1].xcor()
                y_cor = self.segments[i - 1].ycor()
                self.segments[i].teleport(x_cor, y_cor)
            else:
                self.segments[0].forward(20)

    def direction_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def direction_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def direction_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def direction_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
