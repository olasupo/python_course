# Iterating through a list

# Initialize a list of names
names = ["Peter", "Kate", "Dami"]  # A list containing three names: "Peter", "Kate", and "Dami"

# Use a for-loop to iterate over each name in the 'names' list
for name in names:
    # Print each name along with the number of characters it contains using an f-string for formatting
    print(f"{name} has {len(name)} characters only")  # 'len(name)' calculates the length of the string 'name'
