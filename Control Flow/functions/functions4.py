#Example - Default arguments
def addition (a,b = 2):
    result = a + b
    return result,b

def subtraction (a,b =4):
    result = a - b
    return result, b



a = int(input("Please enter a value for a: "))
while True: 
    
    action = input("What do you want to do?: [add, mult, sub, div]: ")
    match action:
        case "add":
            c, b = addition(a)
            print(f"{a} +  {b} = {c}")
        case "sub":
            c, b = subtraction(a)
            print(f"{a} - {b} = {c}")
        case _:
            print ("Sorry, thats an invalid input")
            break
