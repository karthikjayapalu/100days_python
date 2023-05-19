import turtle
import pandas as pd
screen=turtle.Screen()

screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data= pd.read_csv('50_states.csv')

answer_state=screen.textinput(title="Guess the state",prompt="What's another state's name?")
print(answer_state)

# If answer_state is one of the states in all the states of the 50_states.csv
if data['state'] == answer_state:
    #If they got it right:

    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data=data[data['state'] == answer_state]
    t.goto(int(state_data.x),int(state_data.y))
    # Create a turtle to write  the name of the state at the state's x and y coordinate in the image
    t.write(answer_state)

# TODO 1: Convert the guess to Title case
# TODO 2: Check if the guess is among the 50 states
# TODO 3: Write correct guesses onto the map
# TODO 4: Use a loop to allow the user to keep guessing
# TODO 5: Record the correct guesses in a list
# TODO 6: Keep track of the score



# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
