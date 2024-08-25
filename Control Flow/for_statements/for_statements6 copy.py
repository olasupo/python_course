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
