import random

from blackjack_ascii_art import logo

print(logo)

cards = { '2':2, '3':3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K':10, 'A':11 }

def draw_card():
    card = random.choice(list(cards.keys()))
    return card

def get_score(hand):
    score = 0
    for card in hand:
        score += cards[card]

    if score > 21 and 'A' in hand:
        score -= 10

    return score


def print_game_status(user_cards, opponent_cards):
    print(f"Your cards: {user_cards}, current score: {get_score(user_cards)}")
    print(f"Opponent's first card: {opponent_cards[0]}")


def show_full_hands(user_cards, opponent_cards):
    print(f"Your hand: {user_cards}, Opponent's final hand: {opponent_cards}")
    print(f"Your score: {get_score(user_cards)}, Opponent's score: {get_score(opponent_cards)}")

def opponent_hand(opponent_cards):
    while 17 >= get_score(opponent_cards):
        opponent_cards.append(draw_card())

    return opponent_cards


def show_final_result(user_cards, opponent_cards):
    user_score = get_score(user_cards)
    opponent_score = get_score(opponent_cards)
    print(f"Your final hand: {user_cards}, Opponent's final hand: {opponent_cards}")
    print(f"Your score: {user_score}, Opponent's score: {opponent_score}")

    if user_score > 21:
        print("You lost as you went over 21.")
    elif opponent_score > 21:
        print("You win as the opponent went over 21!")
    elif user_score == opponent_score:
        print(f"Both players scored {user_score}, its a push!")
    elif (21-user_score) < (21-opponent_score):
        print("You win!")
    else:
        print("You lose!")


def user_hand(user_cards, opponent_cards):

    play_user_hand = True

    while play_user_hand:
        print_game_status(user_cards, opponent_cards)
        choice = input("Type h to hit or s to stand: ").lower()
        if choice == 's':
            break

        user_cards.append(draw_card())

        if get_score(user_cards) > 21:
            play_user_hand = False
    return user_cards


def handle_initial_draw_blackjack(user_cards, opponent_cards):
    user_score = get_score(user_cards)
    opponent_score = get_score(opponent_cards)

    if user_score == 21 and opponent_score == 21:
        show_full_hands(user_cards, opponent_cards)
        print("Both players got a Blackjack, its a push")
    if user_score == 21:
        show_full_hands(user_cards, opponent_cards)
        print("You won with a Blackjack!")
    elif opponent_score == 21:
        show_full_hands(user_cards, opponent_cards)
        print("You lost as your opponent got a Blackjack!")


def start_blackjack():
    user_cards = [draw_card(), draw_card()]
    opponent_cards = [draw_card(), draw_card()]
    user_score = get_score(user_cards)
    opponent_score = get_score(opponent_cards)

    if user_score == 21 or opponent_score == 21:
        handle_initial_draw_blackjack(user_cards, opponent_cards)
    else:
        user_cards = user_hand(user_cards, opponent_cards)
        if get_score(user_cards) <= 21:
            opponent_cards = opponent_hand(opponent_cards)
        show_final_result(user_cards, opponent_cards)

def blackjack():
    print("Welcome to the game of Blackjack!")
    choice = input("Type y to start the game, n to exit: ").lower()
    if choice == "y":
        start_blackjack()
    else:
        print("See you next time!")

blackjack()