# Example - Looping through a dict

# Creating a dictionary called phonebook
phonebook = {
    "Kunle": "+1 742 230 789",
    "Smart": "+234 904 690 532",
    "Rishi": "+44 798 4322 76",
}

# Variable to search for in the phonebook
eyan = "James"

# Looping through the dictionary keys (names)
for name in phonebook.keys():
    # Checking if 'eyan' is a key in the dictionary
    if eyan in phonebook.keys():
        print(f"{eyan} wa")  # If found, print "{name} wa"
        break
else:
    print("Not found")  # If not found after looping, print "Not found"

# Looping through the dictionary values (phone numbers)
for number in phonebook.values():
    print(number)  # Printing each phone number

# Looping through both keys (names) and values (numbers) in the dictionary
for name, number in phonebook.items():
    print(f"Name: {name} : Number  {number}")  # Printing name and corresponding number
