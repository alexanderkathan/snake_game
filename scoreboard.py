from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Programmieren/Python/snake_game/data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-40, 280)
        self.write(f"Score: {self.current_score} Highscore: {self.high_score}", font=("Arial", 16, "normal"))

    def add_point(self):
        self.current_score = self.current_score + 1
        self.clear()
        self.write(f"Score: {self.current_score} Highscore: {self.high_score}", font=("Arial", 16, "normal"))

    def reset(self):
        if self.current_score > self.high_score:
             self.high_score = self.current_score
             with open("/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Programmieren/Python/snake_game/data.txt", "w") as data:
                 data.write(str(self.high_score))
        self.current_score = 0
        self.clear()
        self.write(f"Score: {self.current_score} Highscore: {self.high_score}", font=("Arial", 16, "normal"))

    # def game_over(self):
    #     self.goto(-30, 0)
    #     self.write(f"GAME OVER", font=("Arial", 16, "normal"))