# exception handling
try:
    num = int(input("Enter your age: "))
except ValueError:
    print("Enter a numerical value for age.")
except Exception as e:
    print(f"There was an error: {e}")
else:
    print(f"Your age is {num}")
finally:
    print("Reading age complete.")


# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0: # it was 'or' in the problem
            print("FizzBuzz")
        elif number % 3 == 0: # it was 'if' in the problem
            print("Fizz")
        elif number % 5 == 0: # it was 'if' in the problem
            print("Buzz")
        else:
            print(f"{number}")

fizz_buzz(10)
