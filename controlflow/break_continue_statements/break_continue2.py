# The continue statement is used to skip the current iteration of the loop and continue with the next iteration

print()  # Print an empty line for separation

# Use a for-loop to iterate over a range of numbers from 2 to 9
for i in range(2, 10):
    # Check if the current number 'i' is even
    if i % 2 == 0:
        print(f"{i} is an Even number")  # Print that the number is even
        continue  # Skip the remaining code in this iteration and continue with the next iteration
    # If the number is not even, print that it is odd
    print(f"{i} is an Odd number.")
