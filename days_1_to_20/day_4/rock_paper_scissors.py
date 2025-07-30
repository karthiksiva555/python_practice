import random
import rock_paper_scissors_ascii

choices = [rock_paper_scissors_ascii.rock, rock_paper_scissors_ascii.paper, rock_paper_scissors_ascii.scissors]

print("Ready to play Rock Paper Scissors?\n")
user_choice = int(input("What do you choose? 0 for rock, 1 for paper and 2 for scissors: "))
computer_choice = random.randint(0, 2)

if user_choice == computer_choice:
    print(f"Both players selected same option: {choices[user_choice]}")
else:
    if user_choice < computer_choice:
        print("You Win!")
    else:
        print("You Lose!")
    print(f"You chose\n{choices[user_choice]}")
    print(f"Computer chose\n{choices[computer_choice]}")

