#Example - keyword arguments or keyword parameters or named parameters
def add (fname,lastname):
    fullname = fname + " " + lastname
    return fullname

lname = input("Please enter your last name: ")

action = input("What do you want to do?: [conc]: ")
match action:
    case "conc" | "Conc":
        fullname = add("Adeyemi", lastname=lname) #lastname is a leyword argument
        print(f"My Fullname is {fullname}")
    case _:
        print ("Sorry, thats an invalid input")
    
    