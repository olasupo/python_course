# Example - using list comprehensions

a = [1, 5, 2]  # Define list 'a' with initial elements [1, 5, 2]
b = [1, 4, 6]  # Define list 'b' with initial elements [1, 4, 6]

# Use a list comprehension to extend list 'a' with the elements of list 'b' if 'a' is not equal to 'b'
[a.extend(b) for i in range(1) if a != b]

print(a)  # Print the modified list 'a'
