from random import randint
from number_guessing_ascii_art import logo

EASY_LEVEL_CHANCES = 10
HARD_LEVEL_CHANCES = 5


def welcome_the_user():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")


def get_chances():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty_level != "easy" and difficulty_level != "hard":
        print(f"{difficulty_level} is an invalid input for difficulty level.")
        return 0

    return EASY_LEVEL_CHANCES if difficulty_level == "easy" else HARD_LEVEL_CHANCES


def get_target():
    return randint(1, 100)


def check_answer(guess, target, chances):
    if guess == target:
        print(f"Your guess {target} is correct, You win!")
    elif guess < target:
        print("Too low.")
    else:
        print("Too high.")

    return 0 if guess == target else chances - 1


def guess_the_number(target, chances):

    while  chances > 0:
        print(f"You have {chances} attempts remaining.")
        guess = int(input("Make a guess: "))
        chances = check_answer(guess, target, chances)

        if chances > 0:
            print("Guess again.")
        elif guess != target:
            print("You have run out of chances. Try again!")


def start_number_guessing_game():
    welcome_the_user()
    chances = get_chances()
    target = get_target()
    print(f"The target is {target}")
    guess_the_number(target, chances)


start_number_guessing_game()

