# Example - Basic Arithmetic and Conditional Statements

a = 5  # Assign the value 5 to variable 'a'
b = 10  # Assign the value 10 to variable 'b'
c = a + b  # Add the values of 'a' and 'b' and assign the result to variable 'c'

# Check if the value of 'a' is less than the value of 'b'
if a < b:
    print(a, "is less than", b)  # If 'a' is less than 'b', print this message
# Check if the value of 'a' is greater than the value of 'b'
elif a > b:
    print(a, "is greater than", b)  # If 'a' is greater than 'b', print this message
# If neither condition above is true, then 'a' must be equal to 'b'
else:
    print(a, "is the same value as", b)  # If 'a' is equal to 'b', print this message
