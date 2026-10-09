"""calc_with_functions.py
Calculator built with functions.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b."""
    return a / b


def calculate(a, b, op):
    """Take two numbers and an operation symbol (+, -, *, /),
    call the correct operation function, and return the result.
    Prints an error message and returns None for an invalid operation.
    """
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        print("Invalid operation! Please use +, -, *, or /.")
        return None


if __name__ == "__main__":
    print("Welcome to my calculator!")
    print("Choose an operation below!")

    # Dictionary mapping symbols to operation names
    operations = {
        "+": "Addition",
        "-": "Subtraction",
        "*": "Multiplication",
        "/": "Division"
    }

    while True:
        print("\n----------------")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        print("\n----------------")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == "5":
            print("Goodbye!!!!")
            break             # <--- Stops the loop

        if choice in ("1", "2", "3", "4"):
            # Map the menu choice to its operation symbol
            op = {"1": "+", "2": "-", "3": "*", "4": "/"}[choice]
            print(f"You chose {operations[op]}")

            # Catch non-numeric inputs for the numbers
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue  # Restarts the loop from the top

            # Use calculate() to get the result.
            # Division by zero is caught here with try/except.
            try:
                result = calculate(num1, num2, op)
            except ZeroDivisionError:
                print("You can't divide by zero!")
                continue  # Restarts the loop from the top

            # calculate() returns None for an invalid operation;
            # otherwise print the answer.
            if result is not None:
                print("The answer is:", result)
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")