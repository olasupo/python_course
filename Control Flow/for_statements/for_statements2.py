# Example - Printing a formatted list of names

# Initialize a list of names
names = ["Peter", "Kate", "Dami"]  # A list containing three names: "Peter", "Kate", and "Dami"

# Print the introductory text before listing the names
print("List of names are: ", end="")  # The 'end=""' ensures that the output remains on the same line

# Use a for-loop to iterate over each name in the 'names' list
for name in names:
    print(name, end=", ")  # Print each name followed by a comma and a space, without moving to the next line
