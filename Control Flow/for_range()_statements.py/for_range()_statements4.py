# Iterate over a list using range

# Initialize a list of names
names = ["Dammy", "Gareth", "Suzie"]  # A list containing three names: "Dammy", "Gareth", and "Suzie"

# Use a for-loop with range and len to iterate over the indices of the list
for i in range(len(names)):
    # Print the index and the corresponding name in the list
    print(f"index {i} is {names[i]}")  
    # 'i' represents the current index in the list, and 'names[i]' accesses the name at that index

# Use the enumerate function to iterate over the list, getting both index and value
for b in enumerate(names):
    # Print the tuple containing the index and the corresponding name
    print(b)
    # Check if the name "Suzie" is in the current tuple
    if "Suzie" in b:
        print("Hurray")  # Print "Hurray" when "Suzie" is found in the list
