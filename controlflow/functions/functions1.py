# Example - Simple function 1

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

# Assign values to 'a' and 'b'
a = 10  # Assign the value 10 to variable 'a'
b = 2   # Assign the value 2 to variable 'b'

# Call the 'addition' function with 'a' and 'b', and store the result in 'c'
c = addition(a, b)  # 'c' will hold the value of 'a' + 'b', which is 12

# Call the 'subtraction' function with 'a' and 'b', and store the result in 'd'
d = subtraction(a, b)  # 'd' will hold the value of 'a' - 'b', which is 8

# Print the results of the addition and subtraction
print(f"{a} + {b} = {c}")  # Output: 10 + 2 = 12
print(f"{a} - {b} = {d}")  # Output: 10 - 2 = 8
