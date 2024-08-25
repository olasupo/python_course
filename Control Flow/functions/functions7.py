# Example - Positional arguments and **kwargs

def combiner(age, **name):
    """
    This function demonstrates the use of a positional argument and **kwargs.
    - 'age' is a positional argument representing the person's age.
    - '**name' collects keyword arguments into a dictionary, where each key-value pair represents a part of the person's name.
    """
    
    # Print the full name using the keyword arguments
    print("My full name is ", end="")
    for i, j in name.items():  # Iterate over the dictionary 'name'
        if i == list(name.keys())[-1]:  # Check if this is the last item in the dictionary
            print(f"{j}", end="\n")  # Print the last name and move to the next line
            print(f"I am {age} years old")  # Print the age after the full name
        else:
            print(f"{j}", end=" ")  # Print the first and middle names followed by a space

# Prompt the user to input their first name, middle name, and last name
fname = input("Please Enter Your First Name: ")
mname = input("Please Enter Your Middle Name: ")
lname = input("Please Enter Your Last Name: ")

# Call the 'combiner' function with the age and name components
fullname = combiner(12, firstName=fname, middleName=mname, lastName=lname)
