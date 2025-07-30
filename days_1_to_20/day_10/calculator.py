from calculator_ascii_art import logo

print(logo)

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

operation_map = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def invoke_operation(num1, num2, operation):
    """Takes two numbers, operation to perform and returns the result"""
    operation_invoker = operation_map[operation]
    return operation_invoker(num1, num2)

def start_calculator():
    num1 = float(input("What is your first number? "))
    use_prev_result = True
    while use_prev_result:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        num2 = float(input("What is your next number? "))
        result = invoke_operation(num1, num2, operation)
        print(f"{num1} {operation} {num2} = {result}")
        next_step = input(f"Type 'y' to continue with {result}, 'n' to start new or 'e' to exit: ")

        if next_step == "e":
            break
        elif next_step == "y":
            num1 = result
        else:
            use_prev_result = False # important: existing loop will continue even after calling the new start_calculator()
            start_calculator()

start_calculator()

