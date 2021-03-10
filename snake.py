from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            self.head = self.all_segments[0]

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1): #start, stop, step
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y) 
        self.all_segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")  
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def up(self):
        if self.all_segments[0].heading() != DOWN:
            self.all_segments[0].setheading(UP)

    def down(self):
        if self.all_segments[0].heading() != UP:
            self.all_segments[0].setheading(DOWN)

    def right(self):
        if self.all_segments[0].heading() != LEFT:
            self.all_segments[0].setheading(RIGHT)
   
    def left(self):
        if self.all_segments[0].heading() != RIGHT:
            self.all_segments[0].setheading(LEFT)
    
    def reset(self):
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]

    def __init__(self):
        self.all_segments = [] 
        self.create_snake()

        