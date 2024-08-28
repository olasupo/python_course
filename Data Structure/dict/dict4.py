# Example - Looping through a dict

# Creating a list of dictionaries, each containing a name and phone number
phonebook = [
     {"Name": "Kunle", "Phone": "+1 742 2340 89"},
     {"Name": "Smart", "Phone": "+234 904 569 532"},
     {"Name": "Rishi", "Phone": "+44 798 432 786"},
]

# Prompting the user to input a name to search for in the phonebook
searchForPerson = input("Enter name to search for: ")

# Looping through each dictionary in the phonebook list
for person in phonebook:
    # Looping through each value in the current dictionary (Name and Phone)
    for values in person.values():
        # Checking if the searched name matches any value in the current dictionary
        if searchForPerson in values:
            print(f"{searchForPerson} found in the phonebook")  # If found, print confirmation
            break  # Exit the loop once found
else:
    print(f"{searchForPerson} not found")  # If not found after looping, print not found
