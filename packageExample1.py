# Example - simple and direct use of packages

# Importing the 'calculator' module from the 'controlflow.functions' package
import controlflow.functions.calculator

# Prompting the user to input an integer value for 'a'
a = int(input("Enter value for a: "))

# Prompting the user to input an integer value for 'b'
b = int(input("Enter value for b: "))

# Using the 'addition' function from the 'calculator' module to add 'a' and 'b'
c = controlflow.functions.calculator.addition(a, b)

# Printing the sum of 'a' and 'b'
print(f"Sum of {a} and {b} is: {c}")
