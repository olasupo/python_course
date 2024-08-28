# Example - User Input and Conditional Statements

# Prompt the user to enter a number for variable 'a' and convert the input to an integer
a = int(input("Please Enter a number for a: "))

# Prompt the user to enter a number for variable 'b' and convert the input to an integer
b = int(input("Please Enter a number for b: "))

# Check if the value of 'a' is less than the value of 'b'
if a < b:
    print(a, "is less than", b)  # If 'a' is less than 'b', print this message

# Check if the value of 'a' is greater than the value of 'b'
elif a > b:
    print(a, "is greater than", b)  # If 'a' is greater than 'b', print this message

# If neither condition above is true, then 'a' must be equal to 'b'
else:
    print(a, "is the same value as", b)  # If 'a' is equal to 'b', print this message
