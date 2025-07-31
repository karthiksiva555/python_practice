piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Get keys 2, 3, 4 Result: ['c', 'd', 'e']
print(piano_keys[2:5])

# Get keys from index 3 to the end, Result: ['d', 'e', 'f', 'g']
print(piano_keys[3:])

# Get keys from beginning to the index 4, result: ['a', 'b', 'c', 'd', 'e']
print(piano_keys[:5])

# Get every other keys Result: ['a', 'c', 'e', 'g']
# Takes a third argument - step up count
print(piano_keys[::2])

# Get every third key starting from index 2, Result: ['c', 'f']
print(piano_keys[2::3])

# Reverse the list; Result: ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(piano_keys[::-1])

# Get second and third from the tuple; Result: ('c', 'd')
piano_keys_tuple = ("a", "b", "c", "d", "e", "f")
print(piano_keys_tuple[2:4])
