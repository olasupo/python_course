# Example - using list comprehensions to conditionally extend a list

# Initializing two lists, 'a' and 'b'
a = [1, 5, 2]
b = [1, 4, 6]

# Using list comprehension to extend list 'a' with list 'b' 
# The comprehension runs for a single iteration (range(1)) 
# and only extends 'a' if 'a' is not equal to 'b'
[a.extend(b) for i in range(1) if a != b]

# Printing the modified list 'a'
print(a)
