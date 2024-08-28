# Example - Keyword Arguments (also known as Keyword Parameters or Named Parameters)

def add(fname, lastname):
    """
    This function takes two arguments: 'fname' (first name) and 'lastname' (last name).
    It concatenates them with a space in between to form a full name.
    """
    fullname = fname + " " + lastname  # Combine first name and last name with a space in between
    return fullname  # Return the full name

# Prompt the user to input their last name
lname = input("Please enter your last name: ")

# Prompt the user to choose an action
action = input("What do you want to do?: [conc]: ")

# Use a match-case structure to handle the user's action
match action:
    case "conc" | "Conc":  # If the action is "conc" (or "Conc"), proceed with concatenation
        fullname = add("Adeyemi", lastname=lname)  # Call the 'add' function with a keyword argument for 'lastname'
        print(f"My Fullname is {fullname}")  # Print the full name
    case _:  # If the action is anything else, handle it as an invalid input
        print("Sorry, that's an invalid input")
