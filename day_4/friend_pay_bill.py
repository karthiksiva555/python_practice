import random

friends = ["Siva", "Ram", "John", "Lila", "Julie"]

random_index = random.randint(0, 4)
print(friends[random_index])

# approach 2
# we can use choice function from random module
friend_to_pay = random.choice(friends)
print(friend_to_pay)