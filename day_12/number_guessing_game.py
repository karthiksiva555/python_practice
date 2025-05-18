import random
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
    return random.randint(1, 100)


def guess_the_number(target, chances):
    attempt = 1

    while attempt <= chances:
        print(f"You have {chances - attempt + 1} attempts remaining.")
        guess = int(input("Make a guess: "))
        if guess == target:
            print(f"Your guess {target} is correct, You win!")
            break
        if guess < target:
            print("Too low.")
        else:
            print("Too high.")

        if attempt == chances:
            print("You have run out of chances. Try again!")
        else:
            print("Guess again.")

        attempt += 1


def start_number_guessing_game():
    welcome_the_user()
    chances = get_chances()
    target = get_target()
    guess_the_number(target, chances)


start_number_guessing_game()

