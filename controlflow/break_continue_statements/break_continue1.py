# The break statement is used to break out of a given for or while loop

# Use a for-loop to iterate over a range of numbers from 2 to 9
for i in range(2, 10):
    # Use a nested for-loop to check divisibility of 'i' by any number from 2 to 'i-1'
    for j in range(2, i):
        # Check if 'i' is divisible by 'j'
        if i % j == 0:
            print(f"{i} is Not a prime number")  # Print that 'i' is not a prime number
            break  # Break out of the inner for-loop as 'i' has a divisor other than 1 and itself
    else:
        # This else statement is executed only if the inner for-loop is not terminated by a break
        print(f"{i} is a Prime number")  # Print that 'i' is a prime number
