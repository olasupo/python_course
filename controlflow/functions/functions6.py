# Example - Positional arguments and *args

def combiner(age, *name):
    """
    This function demonstrates the use of a positional argument and *args.
    - 'age' is a positional argument representing the person's age.
    - '*name' collects additional positional arguments into a tuple, where each element is part of the person's name.
    """
    
    # Print the full name using the positional arguments collected in *name
    print("My full name is ", end="")
    for i in name:  # Iterate over the tuple 'name'
        # Check if the current name part is the last one in the tuple
        # Option 1 (commented out): Check using the index of the element
        # if name.index(i) == len(name) - 1:  # Evaluating index (int) values
        # Option 2 (active): Check by comparing the element directly to the last element
        if i == name[-1]:  # Evaluating string values, i.e., value of the name
            print(f"{i}", end="\n")  # Print the last name part and move to the next line
            print(f"I am {age} years old")  # Print the age after the full name
        else:
            print(f"{i}", end=" ")  # Print the first and middle names followed by a space

# Prompt the user to input their first name, middle name, and last name
fname = input("Please Enter Your First Name: ")
mname = input("Please Enter Your Middle Name: ")
lname = input("Please Enter Your Last Name: ")

# Call the 'combiner' function with the age and name components
fullname = combiner(12, fname, mname, lname)
