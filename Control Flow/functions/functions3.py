# Example - Simple function 3

# Define a function 'addition' that takes two arguments 'a' and 'b'
def addition(a, b):
    """
    This function takes two numbers 'a' and 'b' as input and returns their sum.
    """
    result = a + b  # Calculate the sum of 'a' and 'b'
    return result  # Return the result of the addition

# Define a function 'subtraction' that takes two arguments 'a' and 'b'
def subtraction(a, b):
    """
    This function takes two numbers 'a' and 'b' as input and returns their difference.
    """
    result = a - b  # Calculate the difference between 'a' and 'b'
    return result  # Return the result of the subtraction

# Start an infinite loop to repeatedly prompt the user for input until a valid action is performed or an invalid action breaks the loop
while True:
    # Prompt the user to input a value for 'a'
    a = int(input("Please enter a value for a: "))
    
    # Prompt the user to input a value for 'b'
    b = int(input("Please enter a value for b: "))
    
    # Prompt the user to choose an action from the available options
    action = input("What do you want to do?: [add, mult, sub, div]: ")
    
    # Use a match-case structure to handle the user's action
    match action:
        case "add":
            # If the action is "add", call the 'addition' function with 'a' and 'b'
            c = addition(a, b)
            print(f"{a} + {b} = {c}")  # Print the result of the addition
        case "sub":
            # If the action is "sub", call the 'subtraction' function with 'a' and 'b'
            c = subtraction(a, b)
            print(f"{a} - {b} = {c}")  # Print the result of the subtraction
        case _:
            # If the action does not match "add" or "sub", print an error message and break the loop
            print("Sorry, that's an invalid input")
            break  # Exit the loop
