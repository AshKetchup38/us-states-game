import turtle
import pandas
from scoreboard import Scoreboard


screen = turtle.Screen()
score = Scoreboard()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
guessed_states = []
missed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) != 50:
    total_score = score.get_score()
    answer = screen.textinput(f"{total_score}/50 States Correct", "Enter a state: ").title()
    answer_found = data[data.state == answer]
    if answer in guessed_states:
        guessed_states.append(answer)
    else:
        if answer_found.empty == False:
            guessed_states.append(answer)
            x = int(answer_found["x"])
            y = int(answer_found["y"])
            score.increase_score()
            score.label(answer,x,y)
        else:
            guessed_states.append(answer)
    print(guessed_states)

score.print_gameover()
for state in all_states:
    if state not in guessed_states:
        missed_state = data[data.state == state]
        missed_x = int(missed_state["x"])
        missed_y = int(missed_state["y"])
        score.label_missed(state,missed_x,missed_y)

turtle.mainloop()