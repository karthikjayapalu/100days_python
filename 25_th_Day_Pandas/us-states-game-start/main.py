import turtle
import pandas as pd
screen=turtle.Screen()

screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data= pd.read_csv('50_states.csv')


all_states=data.state.to_list()
guessed_states=[]
# print(answer_state)

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct ",
                                    prompt="What's another state's name?").title()
    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state =="Exit":

        # states to learn.csv
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        #If they got it right:
        guessed_states.append(answer_state)
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
