# Example - Looping through a dict

# Creating a list of dictionaries, each containing a name and phone number
phonebook = [
     {"Name": "Kunle", "Phone": "+1 742 240 789"},
     {"Name": "Smart", "Phone": "+234 904 590 532"},
     {"Name": "Rishi", "Phone": "+44 798 432 786"},
]

# Looping through the list of dictionaries to print each person's name
for person in phonebook:
    print(person["Name"])  # Accessing and printing the "Name" key from each dictionary

# Looping through the list of dictionaries to print each person's phone number
for number in phonebook:
    print(number["Phone"])  # Accessing and printing the "Phone" key from each dictionary
