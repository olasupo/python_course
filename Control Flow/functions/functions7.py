#Example - positional arguments and **kwargs
def combiner(age, **name):
    print("My full name is ", end="")
    for i,j in name.items():
        if i == list(name)[-1]:
           print(f"{j}", end="\n")
           print(f"I am {age} years old")
        else:
            print(f"{j}", end=" ")

fname = input("Please Your First Name: ")
mname = input("Please Your Middle Name: ")
lname = input("Please Your Last Name: ")

fullname = combiner(12, firstName = fname, middleName = mname,lastName = lname)