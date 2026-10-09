def greet_user(name=""):
    """Take a name (string) and print a greeting.

    If no name is provided (empty string or default), print a
    generic greeting: "Hello! Welcome!"
    """
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello! Welcome!")


def add_two_numbers(a, b):
    """Return the sum of two numbers a and b."""
    return a + b


def is_even(num):
    """Return True if num is even, False otherwise."""
    return num % 2 == 0


if __name__ == "__main__":
    # --- Demonstrate greet_user() ---
    # Called with a sample name:
    greet_user("Alice")
    # Called without a name (uses the default empty string):
    greet_user()

    # --- Demonstrate add_two_numbers() ---
    # The returned value is stored in a variable, then printed:
    sum_result = add_two_numbers(7, 5)
    print(f"The sum of 7 and 5 is: {sum_result}")
    # The return value can also be used directly in an expression:
    print("7 + 5 + 10 =", add_two_numbers(7, 5) + 10)

    # --- Demonstrate is_even() ---
    # Test an even number and an odd number:
    four_even = is_even(4)
    print(f"4 is even: {four_even}")      # stored in a variable first
    print(f"7 is even: {is_even(7)}")     # used directly in the expression
    # The boolean result can also drive other logic:
    check = 10
    print(f"{check} is even: {is_even(check)}")