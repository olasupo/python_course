# Example - Age Group Classification with match-case

def tribe(response):
    """
    This function takes an age as input and returns the corresponding age group classification.
    It uses a match-case structure to handle different age ranges.
    """
    match response:
        case a if response in range(0, 2):
            return "Baby"  # Age 0-1: Baby
        case b if response in range(2, 6):
            return "Toddler"  # Age 2-5: Toddler
        case c if response in range(6, 13):
            return "Adolescent"  # Age 6-12: Adolescent
        case d if response in range(13, 20):
            return "Teenager"  # Age 13-19: Teenager
        case e if response >= 20 and response <= 100:
            return "Adult"  # Age 20-100: Adult
        case _:
            return "Not Likely a valid value"  # Any other value: Not a recognized age range
        
# Start of the loop to continuously prompt for age input until the user enters -1
response = 0
while response != -1:
    response = int(input("Please input your age? "))  # Prompt the user to enter their age
    age_group = tribe(response)  # Call the tribe function with the provided age
    print(f"You are in the {age_group} age group")  # Print the corresponding age group classification
