# Example - Iterating over a list and counting characters

# Initialize a list of names
names = ["Peter", "Kate", "Dami"]  # A list containing three names: "Peter", "Kate", and "Dami"

# Use a for-loop to iterate over each name in the 'names' list
for name in names:
    # Print each name along with the number of characters it contains
    print(name, "has", len(name), "characters")  # 'len(name)' calculates the length of the string 'name'
