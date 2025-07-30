print("Welcome to the rollercoaster!\n")
height = int(input("Enter your height in cm: "))
total = 0

if height >= 120:
    age = int(input("Enter your age: "))
    if age<=12:
        total = 5
    elif age <= 18:
        total = 7
    else:
        total = 12

    want_photo = input("Want to take photo? type y for yes and n for no: ")
    if want_photo == 'y' or want_photo == 'Y':
        total += 3

    print(f"Your total bill is : ${total}")
else:
    print("Sorry, you have to grow taller to ride.")

