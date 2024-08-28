# Iterating through a dictionary

# Initialize a dictionary 'person' with key-value pairs representing personal information
person = {"fname": "Olasupo", "lname": "Okunaiya", "age": 39, "height": "1.7m"}  
# The dictionary contains the following key-value pairs:
# "fname" (first name) -> "Olasupo"
# "lname" (last name) -> "Okunaiya"
# "age" -> 39
# "height" -> "1.7m"

# Initialize an empty list 'placeholder' (though it's not used in this loop)
placeholder = []

# Use a for-loop to iterate over each key-value pair in the 'person' dictionary
for key, value in person.items():
    # Print the key and its corresponding value
    print(key, value)  
    # 'key' represents the current key in the dictionary (e.g., "fname", "lname", etc.)
    # 'value' represents the value associated with the current key (e.g., "Olasupo", "Okunaiya", etc.)

    # Check if the current key is "lname"
    if key == "lname":
        continue  # Skip the rest of the code in this loop iteration and move to the next key-value pair
        print("We will NOT stop here")  # This line will never be executed due to the 'continue' statement
    
    # Check if the current value is 39
    elif value == 39:
        person[key] = value + 10  # Update the "age" key with a new value (39 + 10 = 49)
        print(f"He is {value} years old")  # Print the current value of "age"
        break  # Exit the loop after updating the age

# Print the modified dictionary
print(person)  
# The output will show the dictionary with the updated "age" if the loop was not terminated earlier
