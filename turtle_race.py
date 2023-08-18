import turtle
from turtle import Turtle, Screen
import random
from time import sleep

screen = Screen()
screen.setup(width=500, height=400)
turtle_colors = ["pink", "blue", "green", "yellow", "orange", "red"]

x = -230
y = -100
my_turtles = []
for i in range(6):
    debo = Turtle(shape="turtle")
    debo.color(turtle_colors[i])
    debo.penup()
    debo.goto(x, y)
    y += 40
    my_turtles.append(debo)

user_bet = screen.textinput(title="Turtle Race Betting", prompt="Which turtle would you bet your life on?")

is_race_on = True
while is_race_on:
    for _ in my_turtles:
        dist = random.randint(1, 10)
        _.forward(dist)
        if _.xcor() >= 220:
            is_race_on = False
            winner = _.pencolor()
            break
# print(winner)

if user_bet == winner:
    print(f"Hurray!!!{winner} turtle won the race.")
    sleep(2)
    screen.clearscreen()
    turtle.bgpic("img.png")
else:
    print(f"You lost your money...{winner} turtle won the race.")
    sleep(2)
    screen.clearscreen()
    turtle.bgpic("lose.png")

screen.exitonclick()
