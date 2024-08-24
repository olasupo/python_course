#Example - Unpacking**kwargs
def combiner(age, firstName, middleName, lastName):
    print(f"My full name is {firstName}, {middleName}, {lastName}. I am {age} years old")
    

fname = input("Please Your First Name: ")
mname = input("Please Your Middle Name: ")
lname = input("Please Your Last Name: ")


person = {"firstName":fname,"middleName":mname, "lastName":lname}

fullname = combiner(12, **person)