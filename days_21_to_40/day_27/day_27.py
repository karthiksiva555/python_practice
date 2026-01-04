# Without Default values
def my_method(a, b, c):
    print(f"Arguments received are: a={a}, b={b}, c={c}")

my_method(10, 20, 30) # Positional arguments
my_method(b=20, c=30, a=10) # Keyword arguments

# With Default values
def my_smart_method(a=10, b=20, c=30):
    print(f"Arguments received are: a={a}, b={b}, c={c}")

my_smart_method()
my_smart_method(b=25)
my_smart_method(c=50, a=35)

# unlimited number of arguments
def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(add(1, 2, 3))
print(add(20, 30, 40 ,50, 60))
print(add())

# Unlimited Keyword Arguments
# if add or multiply keywords are not supplied, an error will be thrown
def calculate(n, **kwargs):
    print(kwargs) # {'add': 5, 'multiply': 10}
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(10, add=5, multiply=10)) # 150

# Unlimited keyword arguments - safe
# No error will be thrown even if the keywords add or multiply are not supplied
def calculate_safe(n, **kwargs):
    print(kwargs)
    n += kwargs.get("add", 0)
    n *= kwargs.get("multiply", 1)
    return n

print(calculate_safe(10, add=5)) # 15
print(calculate_safe(10, multiply=5)) # 50