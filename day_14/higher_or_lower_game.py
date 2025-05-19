from art import logo, versus
from game_data import data
from random import choice


# show welcome message
def show_welcome_message():
    print(logo)


# pick a random celebrity
def pick_celebrity():
    return choice(data)


# show celebrity description
def show_celebrity(celebrity):
    description = celebrity["description"].lower()
    salutation = "an" if description[0] == 'a' else "a"
    return f"{celebrity['name']}, {salutation} {celebrity['description']} from {celebrity['country']}"


def show_comparison(celebrity_a, celebrity_b):
    print(f"Compare A: {show_celebrity(celebrity_a)}")
    print(versus)
    print(f"Against B: {show_celebrity(celebrity_b)}")


def get_winner(celebrity_a, celebrity_b):
    return "A" if celebrity_a['follower_count'] > celebrity_b['follower_count'] else "B"


def get_user_guess():
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return choice


# pick initial two
def start_game():
    show_welcome_message()
    celebrity_a = pick_celebrity()
    celebrity_b = pick_celebrity()
    stop_game = False
    score = 0
    while not stop_game:
        show_comparison(celebrity_a, celebrity_b)
        winner = get_winner(celebrity_a, celebrity_b)
        user_guess = get_user_guess()
        if winner == user_guess:
            score += 1
            print(f"You guessed it right! your current score is {score}.")
            celebrity_a = celebrity_b if winner == "B" else celebrity_a
            celebrity_b = pick_celebrity()
        else:
            print(f"Sorry, that is wrong. Your final score is {score}.")
            stop_game = True


start_game()



