# Example - ValueError handling in a try-except block

# Start an infinite loop to keep prompting the user until valid input is received
while True:
    try:
        # Prompt the user to enter an integer for 'a'
        a = int(input("Please enter a number for a: "))
        
        # Prompt the user to enter an integer for 'b'
        b = int(input("Please enter a number for b: "))
        
        # If both inputs are valid integers, exit the loop
        break
    except:
        # If a ValueError occurs (invalid input), print an error message
        if ValueError:
            print("That's an invalid input")

# Calculate and print the sum of 'a' and 'b'
print(f"Sum of {a} and {b} is {a+b}")
