#Example - positional arguments and *args
def combiner(age, *name):
    print("My full name is ", end="")
    for i in name:
        #if name.index(i) == len(name)-1: #Evaluating index (int) values. Does thesame thing as the line below.
        if i == name[-1]: #evaluating string values, i.e value of name
           print(f"{i}", end="\n")
           print(f"I am {age} years old")
           
        else:
            print(f"{i}", end=" ")

fname = input("Please Your First Name: ")
mname = input("Please Your Middle Name: ")
lname = input("Please Your Last Name: ")

fullname = combiner(12, fname, mname,lname)