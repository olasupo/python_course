# Example - use of packages

# Importing the 'addition' function directly from the 'calculator' module
# within the 'controlflow.functions' package
from controlflow.functions.calculator import addition

# Prompting the user to input an integer value for 'a'
a = int(input("Enter value for a: "))

# Prompting the user to input an integer value for 'b'
b = int(input("Enter value for b: "))

# Calling the 'addition' function to calculate the sum of 'a' and 'b'
c = addition(a, b)

# Printing the sum of 'a' and 'b'
print(f"Sum of {a} and {b} is: {c}")
