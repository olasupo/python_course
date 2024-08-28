# Iterating through a string

# Initialize the string 'name' to iterate over
name = "Peter"  # The string containing the name "Peter"

# Initialize an empty list 'placeholder' to store characters as they are encountered
placeholder = []

# Use a for-loop to iterate over each character in the string 'name'
for char in name:
    j = name.index(char)  # Find the index of the current character 'char' in the string 'name'
    
    # Append the current character 'char' to the 'placeholder' list
    placeholder.append(char)
    
    # Print the current state of the 'placeholder' list
    print(placeholder, end="")
    
    # Check if the current character 'char' has appeared more than once in 'placeholder'
    if placeholder.count(char) > 1:
        pc = placeholder.count(char)  # Count how many times 'char' has occurred in 'placeholder'
        print(f"{char} has occurred {pc} times")  # Print how many times the character has occurred
        break  # Exit the loop if the character has occurred more than once
    
    # Check if the length of 'placeholder' has exceeded 2 characters
    if len(placeholder) > 2:
        print(f"length of placeholder is {len(placeholder)}")  # Print the length of 'placeholder'
        break  # Exit the loop if the length of 'placeholder' is greater than 2
