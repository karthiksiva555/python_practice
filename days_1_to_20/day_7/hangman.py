import random
import hangman_ascii_art
import hangman_words


print(hangman_ascii_art.logo)
print("Welcome to the hangman game!")

selected_word = random.choice(hangman_words.word_list)


def get_updated_placeholder(chosen_word, guess_char, placeholder_string):
    placeholder_array = list(placeholder_string)
    for index in range(len(placeholder_array)):
        if chosen_word[index] == guess_char:
            placeholder_array[index] = guess_char
    return ''.join(placeholder_array)


lives = 6
placeholder = "_"*len(selected_word)
print(f"{placeholder}")

game_over = False

while not game_over:
    guess = input("Enter your guess: ").lower()
    decision = ""
    if guess in placeholder:
        decision = "already made, try a new character"
    elif guess in selected_word:
        placeholder = get_updated_placeholder(selected_word, guess, placeholder)
        decision = "right"
    else:
        lives -= 1
        decision = "wrong"
    game_over = lives == 0 or "_" not in placeholder

    if not game_over:
        print(f"Your guess was {decision}. You have {lives}/6 lives.")

    print(f"{hangman_ascii_art.stages[lives]}")
    print(placeholder)


if lives == 0:
    print("You ran out of lives, you lose.")
else:
    print("You have guessed the word right! You win.")