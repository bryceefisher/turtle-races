from turtle import Turtle, Screen
from random import randint

def check_winner(winner, user_bet):
    if user_bet == winner:
        print(f"You got it right, the winner was {winner}.")
    else:
        print(f"You got it wrong, the winner was {winner}.")


is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ").lower()

if user_bet:
    is_race_on = True

colors = ["red", "orange", "yellow", "green", "blue", "violet"]

y_positions = [-125, -75, -25, 25, 75, 125]

all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(-230, y_positions[turtle_index])
    all_turtles.append(tim)


turtle = 0
while is_race_on:
    for turtle in all_turtles:
        random_number = randint(0, 10)
        turtle.forward(random_number)
        if turtle.xcor() >= 230:
            winner = turtle.color()[0]
            is_race_on = False
            check_winner(winner, user_bet)










screen.exitonclick()
