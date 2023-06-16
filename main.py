import turtle
import pandas
from scoreboard import Scoreboard


screen = turtle.Screen()
score = Scoreboard()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
total_guesses = 0

while total_guesses != 50:
    total_score = score.get_score()
    answer = screen.textinput(f"{total_score}/50 States Correct", "Enter a state: ")

    data = pandas.read_csv("50_states.csv")
    answer_found = data[data.state == answer]
    if answer_found.empty:
        total_guesses += 1

    else:
        total_guesses += 1
        x = int(answer_found["x"])
        y = int(answer_found["y"])
        score.increase_score()
        score.label(answer,x,y)

score.print_gameover()

turtle.mainloop()