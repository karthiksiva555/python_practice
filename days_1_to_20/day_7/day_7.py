# print each character in a string
name = "siva karthik"
for ch in name:
    print(ch)

# convert string to char array using list()
name_as_array = list(name)
print(name_as_array)

# cannot edit a string by one of its index
# name[0] = 'S' # won't work

title = "software development"
title_as_array = list(title)
title_as_array[0] = 'S'
title_as_array[9] = 'D'
new_title = ''.join(title_as_array)
print(new_title) # Software Development

# find out if a character exists in a string
animal_name = "elephant"
if 'e' in animal_name:
    print("character exists in name")
else:
    print("character doesn't exist in name")
