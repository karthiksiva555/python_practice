print("Welcome to the tip calculator!\n")
# total_str = input("Enter the total bill amount: $")
# total = float(total_str)
# tip_percent_str = input("Enter the tip percentage: ")
# tip_percent = float(tip_percent_str)
# number_of_people_str = input("How many people you are splitting the bill with? ")
# number_of_people = int(number_of_people_str)

total = float(input("Enter the total bill amount: $"))
tip_percent = float(input("Enter the tip percentage: "))
number_of_people = int(input("How many people you are splitting the bill with? "))

total_with_tips = total + (total*tip_percent/100)
per_head = total_with_tips/number_of_people

# round per_head to two decimal places
print(f"Each person should pay ${per_head:.2f}")