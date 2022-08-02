import pandas
from turtle import *

screen = Screen()
screen.setup(height=491, width=725)
screen.bgpic("C:/Thesis/Day 24/us-states-game-start/blank_states_img.gif")

data = pandas.read_csv("C:/Thesis/Day 24/us-states-game-start/50_states.csv")
game_is_on =True

score_writer = Turtle()
score_writer.hideturtle()
score_writer.penup()
writer=Turtle()
writer.hideturtle()
writer.penup()
writer.goto(310,200)
writer.pendown()
writer.write("/50", align='center', font=("Courier", 25, "normal"))
writer.penup()
states = data.state.to_list()

#print(states)
#print(data)
correct_states = []
score = 0
while game_is_on:
    answer = screen.textinput("States Quiz",'Name a U.S State').title()
    if answer == "Exit":
        print(f"Your score was {score}/50!\nHere are the states you missed:")
        missing_states = [ state for state in states if state not in correct_states ]
        for i in missing_states:
            print(i)

        break
    for i in states:
        if i == answer and answer not in correct_states:

            finder = data[data.state==i]
            #print(finder)
            correct_state = finder['state'].to_list()

            correct_states.append(correct_state[0])
            if answer in correct_states:
                score +=1
                score_writer.clear()
                score_writer.goto(270, 200)
                score_writer.pendown()
                score_writer.write(score, align='center', font=("Courier", 25, "normal"))
            #print(correct_states)
            writer.goto(int(finder.x),int(finder.y))
            writer.write(i)





screen.exitonclick()