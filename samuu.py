def add_numbers(*args):
    """
    Adds any number of numbers passed as arguments.

    Args:
        *args: A variable number of numeric arguments.

    Returns:
        int or float: The sum of all the numbers.
    """
    return sum(args)

# Calling the function with multiple arguments
result = add_numbers(1, 2, 3, 4, 5)
print(f"The result of adding numbers is: {result}")


