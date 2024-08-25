# Example - HTTP Response Code Handling with match-case

def hppt(response_code):
    """
    This function takes an HTTP response code as input and returns a corresponding message.
    It uses a match-case structure to handle various HTTP response codes.
    """
    match response_code:
        case 200:
            return "Okay"  
        case 201:
            return "Updated"  
        case 404:
            return "Page Not Found"  
        case 403:
            return "Unauthorized" 
        case 500:
            return "Internal Server Error"  
        case _:
            return "Not Likely a valid value"  # Any other value: Not a recognized HTTP response code
        
# Start of the loop to continuously prompt for HTTP response codes until the user enters -1
response_code  = 0      
while response_code != -1:
    response_code = int(input("Enter An HTTP response code? "))  # Prompt the user to enter an HTTP response code
    http_response = hppt(response_code)  # Call the hppt function with the provided response code
    print(f"Page Request returned {response_code} : {http_response}")  # Print the response message based on the provided code
