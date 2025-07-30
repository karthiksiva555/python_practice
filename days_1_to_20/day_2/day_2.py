# data types, Numbers, Operations, f-strings, type conversions

# string is an array of characters
greeting = "Hello"
print(f"Character at {0}: {greeting[0]}")
# negative index gives us the item at that position from backwards
print(f"Second character from last: {greeting[-2]}")

# type() is an in-built function to find out the type of the data
print(type(greeting))

# data read from input() is of type string
# print(type(input("Enter your Age: "))) # str

# Data Types: str, float, int, bool
name = "siva"
print(type(name)) # str

num = 123
print(type(num)) # int

amount = 12.50
print(type(amount)) # float

is_admin = True
print(type(is_admin)) # bool

# for better readability, we can use _ to separate a long number.
# Compiler just ignores the underscore _.
long_num = 123_456_7890
print(long_num) # 1234567890

# type casting: str(), int(), float(), bool()
num_str = "123"
print(int(num_str))

float_str = "12.45"
print(float(float_str))

bool_str = "True"
print(bool(bool_str))

print("To string " + str(123))

# Type Errors: Python throws ValueError when the type casting fails
# ValueError: invalid literal for int() with base 10: 'abc'
# print(int("abc"))

# ValueError: could not convert string to float: 'abc'
# print(float("abc"))

# Boolean Type casting is special:
# all non-empty data is evaluated to true and all empty data to false
print(bool("abc")) # True
print(bool("")) # False
print(bool([1, 2])) # True
print(bool([])) # False

# Operators
# Operator precedence: PEMDAS => Parenthesis, Exponent, Multiplication, Division, Add, Subtract

# division results in float by default
print(6/3) # 2.0
# Floor division => returns only the integer part of the result
print(6//3) # 2

# assignment operators: +=, -=, *=, /=
num = 5
num += 4
print(num)

num -= 2
print(num)

num *= 3
print(num)

num /= 7
print(num)

# exponent operator: **
print(2**3) # 8 (2 * 2 * 2)

# round()
result = 8/3
print(result) # 2.66666666666
print(round(result)) # rounds to nearest integer : 3
print(round(result, 2)) # rounds to two decimal places: 2.67

# format string
print(f"Result rounded to two decimal places: {result:.2f}")

# round() vs :.2f
# round() uses banker's rounding where halves are rounded to nearest even
print(round(4.5)) # 4 because 4 is the nearest even
print(round(5.5)) # 6

# format string :.2f uses standard routing, main purpose is to format the string
print(f"{4.578:.2f}") # 4.58
print(f"{4.8:.2f}") # 4.80

# complex primitive type;
# j is reserved in python when it has a numeric value before it
a = 4 + 3j
b = 5 - 2j
c = a + b
print(c) # (9 + 1j)

d = complex(3, 4)
e = complex(2, -6)
print(d+e) # (5 - 2j)

# None primitive type
no_value = None
print(no_value) # None
print(type(no_value)) # <class 'NoneType'>






