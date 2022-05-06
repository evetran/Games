from art import logo


print(logo)


# Functions of operations
def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1/number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculation():
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    stop_calculator = False
    while not stop_calculator:
        operation = input("Pick an operation ")
        num2 = float(input("What is the next number? "))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        continue_calculation = input("Do you want to continue calculating the result? "
                                     "Type 'y' to continue and 'n' to restart").lower()
        if continue_calculation == "y":
            num1 = result
        else:
            stop_calculator = True
            calculation()


calculation()