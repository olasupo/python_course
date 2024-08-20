def execute(command,ls):
    
    match command.split():
        case ["add", value]:
            if value in ls:
                return ls
            else:
                ls.append(value)
                return ls
        case ["minus", value]:
            ls.pop(ls.index(value))
            return ls
        case _:
            print("Unknown Command")
            return value



names=["Ade", "Rishi", "Stone"]
command = ""
value=[]
while command != "quit":
    command = input(">>>")
    new_names = execute(command, names)
    print(f"New value is {new_names}")