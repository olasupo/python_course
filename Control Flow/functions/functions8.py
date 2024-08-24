#Example - positional arguments, *args and **kwargs
def combiner(age, *args, **name):
    print("My full name is ", end="")
    for i,j in name.items():
        if i == list(name)[-1]:
           print(f"{j}", end="\n")
           print(f"I am {age} years old")
        else:
            print(f"{j}", end=" ")
    print(f"My first and Second Laguages are:", end=" ")
    
    for k in args:
        if k == args[-1]:
            print(f"{k}", end="\n")
            print("The End...")
        else:
            print(f"{k}", end=" and ")

fname = input("Please Your First Name: ")
mname = input("Please Your Middle Name: ")
lname = input("Please Your Last Name: ")
flanguage = input("Please Input Your First Language: ")
slanguage = input("Please Input Your Second Language: ")

fullname = combiner(12, flanguage, slanguage, firstName = fname, middleName = mname,lastName = lname)