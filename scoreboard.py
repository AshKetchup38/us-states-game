from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def print_gameover(self):
        self.color("black")
        self.setposition(0, 280)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)
    
    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score
    
    def label(self, name, x, y):
        self.color("black")
        self.setposition(x, y)
        self.write(f"{name}", False, ALIGNMENT, FONT)
    
    def label_missed(self, name, x, y):
        self.color("red")
        self.setposition(x, y)
        self.write(f"{name}", False, ALIGNMENT, FONT)