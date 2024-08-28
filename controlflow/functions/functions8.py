# Example - Positional arguments, *args, and **kwargs

def combiner(age, *args, **name):
    """
    This function demonstrates the use of positional arguments, *args, and **kwargs.
    - 'age' is a positional argument.
    - '*args' collects additional positional arguments into a tuple.
    - '**name' collects keyword arguments into a dictionary.
    """
    
    # Print the full name using the keyword arguments
    print("My full name is ", end="")
    for i, j in name.items():  # Iterate over the dictionary 'name'
        if i == list(name)[-1]:  # Check if this is the last item in the dictionary
            print(f"{j}", end="\n")  # Print the last name and move to the next line
            print(f"I am {age} years old")  # Print the age after the full name
        else:
            print(f"{j}", end=" ")  # Print the first and middle names followed by a space
    
    # Print the languages using the positional arguments in *args
    print(f"My first and second languages are:", end=" ")
    for k in args:  # Iterate over the tuple 'args'
        if k == args[-1]:  # Check if this is the last language in the tuple
            print(f"{k}", end="\n")  # Print the last language and move to the next line
            print("The End...")  # Print a closing message
        else:
            print(f"{k}", end=" and ")  # Print the languages separated by " and "

# Prompt the user to input their name and languages
fname = input("Please Enter Your First Name: ")
mname = input("Please Enter Your Middle Name: ")
lname = input("Please Enter Your Last Name: ")
flanguage = input("Please Enter Your First Language: ")
slanguage = input("Please Enter Your Second Language: ")

# Call the 'combiner' function with the age, languages, and name components
fullname = combiner(12, flanguage, slanguage, firstName=fname, middleName=mname, lastName=lname)
