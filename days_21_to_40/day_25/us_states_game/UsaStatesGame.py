import turtle
import pandas


class UsaStatesGame:

    IMAGE_PATH = "blank_states_img.gif"
    COORDINATES_PATH = "50_states.csv"

    def __init__(self):
        self.screen = turtle.Screen()
        self.setup_screen()
        self.state_coordinates = pandas.read_csv(self.COORDINATES_PATH)
        self.answered_states = []
        self.continue_game = False

    def setup_screen(self):
        self.screen.title("U.S.A States Game")
        self.screen.addshape(self.IMAGE_PATH)
        turtle.shape(self.IMAGE_PATH)

    def start_game(self):
        self.continue_game = True

        while self.continue_game:
            user_input = self.get_user_input()
            if user_input is None:
                self.continue_game = False
            else:
                self.process_user_input(user_input)
                if len(self.answered_states) >= 50:
                    self.continue_game = False

    def get_user_input(self):
        answered_count = len(self.answered_states)
        title = f"{answered_count}/50 States Correct"
        choice = self.screen.textinput(title=title, prompt="What is the other state's name?")
        return choice

    def process_user_input(self, user_input):
        state_details = self.state_coordinates[self.state_coordinates["state"] == user_input]
        if not state_details.empty:
            state_name = state_details.state.item()
            coordinates = (state_details.x.item(), state_details.y.item())
            self.set_answered_state(state_name, coordinates)
            self.answered_states.append(state_name)

    @staticmethod
    def set_answered_state(state_name, coordinates):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(coordinates)
        t.write(state_name)

