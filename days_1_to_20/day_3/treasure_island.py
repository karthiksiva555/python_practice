print(r'''
   _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")
answer = input("You are at a cross road, where do you want to go? type left or right: ")
if answer != "left":
    print("You fell into a hole. Game Over")
else:
    answer = input("You have come to a lake. There is an island in the middle of the lake.\n Type \"wait\" to wait for the boat or \"swim\" to swim across.\n")
    if answer != "wait":
        print("You were attacked by a trout. Game Over.")
    else:
        answer = input("You arrived at the island unharmed. There is a house with three doors.\nOne red, one yellow and one blue. Which colour do you choose?\n")
        if answer == 'red':
            print("It is a room full of fire. Game Over.")
        elif answer == "yellow":
            print("You found the treasure, You win!")
        elif answer == "blue":
            print("You were eaten by beasts. Game Over.")
        else:
            print("You didn't enter any rooms. Game OVer.")



