#Example - Simple function 3
def addition (a,b):
    result = a + b
    return result

def subtraction (a,b):
    result = a - b
    return result

while True: 
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))
    action = input("What do you want to do?: [add, mult, sub, div]: ")
    match action:
        case "add":
            c = addition(a,b)
            print(f"{a} + {b} = {c}")
        case "sub":
            c = subtraction(a,b)
            print(f"{a} - {b} = {c}")
        case _:
            print ("Sorry, thats an invalid input")
            break