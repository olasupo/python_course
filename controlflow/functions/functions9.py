# Example - Unpacking **kwargs

def combiner(age, firstName, middleName, lastName):
    """
    This function takes an age and three name components (first, middle, and last) as arguments.
    It then prints out a formatted string that includes the full name and age.
    """
    print(f"My full name is {firstName}, {middleName}, {lastName}. I am {age} years old")
    
# Prompt the user to enter their first name, middle name, and last name
fname = input("Please Enter Your First Name: ")
mname = input("Please Enter Your Middle Name: ")
lname = input("Please Enter Your Last Name: ")

# Create a dictionary 'person' to store the user's name components
person = {"firstName": fname, "middleName": mname, "lastName": lname}

# Call the 'combiner' function with the age 12 and unpack the 'person' dictionary into keyword arguments
fullname = combiner(12, **person)
