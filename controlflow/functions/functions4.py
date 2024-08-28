# Example - Default Arguments

def addition(a, b=2):
    """
    This function takes two arguments: 'a' and 'b'.
    - 'a' is a required positional argument.
    - 'b' is an optional argument with a default value of 2.
    The function returns the sum of 'a' and 'b', and also returns the value of 'b'.
    """
    result = a + b  # Calculate the sum of 'a' and 'b'
    return result, b  # Return the result and the value of 'b'

def subtraction(a, b=4):
    """
    This function takes two arguments: 'a' and 'b'.
    - 'a' is a required positional argument.
    - 'b' is an optional argument with a default value of 4.
    The function returns the result of subtracting 'b' from 'a', and also returns the value of 'b'.
    """
    result = a - b  # Calculate the result of 'a' minus 'b'
    return result, b  # Return the result and the value of 'b'

# Prompt the user to input a value for 'a'
a = int(input("Please enter a value for a: "))

# Start a loop that will repeatedly ask the user to choose an action
while True:
    # Prompt the user to choose an action
    action = input("What do you want to do?: [add, mult, sub, div]: ")
    
    # Use a match-case structure to handle the user's action
    match action:
        case "add":
            # If the action is "add", call the 'addition' function with the value of 'a'
            c, b = addition(a)  # 'b' will use its default value of 2 unless otherwise specified
            print(f"{a} + {b} = {c}")  # Print the result of the addition
        case "sub":
            # If the action is "sub", call the 'subtraction' function with the value of 'a'
            c, b = subtraction(a)  # 'b' will use its default value of 4 unless otherwise specified
            print(f"{a} - {b} = {c}")  # Print the result of the subtraction
        case _:
            # If the action does not match "add" or "sub", print an error message and break the loop
            print("Sorry, that's an invalid input")
            break  # Exit the loop
