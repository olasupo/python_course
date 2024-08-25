# Example - Command Execution with match-case using split

def execute(command, ls):
    """
    This function takes a command string and a list, then executes the command on the list.
    It uses a match-case structure to handle different commands: "add" and "minus".
    """
    
    # Split the command string into a list of words and match the pattern
    match command.split():
        case ["add", value]:
            # If the command is "add" and the value is not already in the list, append it
            if value in ls:
                return ls  # Return the list unchanged if the value is already present
            else:
                ls.append(value)  # Append the value to the list
                return ls  # Return the updated list
        case ["minus", value]:
            # If the command is "minus", remove the value from the list by finding its index
            ls.pop(ls.index(value))
            return ls  # Return the updated list
        case _:
            # If the command does not match any known patterns, print an error message
            print("Unknown Command")
            return value  # Return the value (empty or last command input) if the command is unknown

# Initial list of names
names = ["Ade", "Rishi", "Stone"]

# Start of the loop to continuously prompt for commands until the user enters "quit"
command = ""
value = []
while command != "quit":
    command = input(">>>")  # Prompt the user to enter a command
    new_names = execute(command, names)  # Call the execute function with the command and the list
    print(f"New value is {new_names}")  # Print the updated list after the command is executed
