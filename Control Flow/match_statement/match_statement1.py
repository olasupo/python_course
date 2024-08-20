def hppt(response_code):
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
            return "Not Likely a valid value"
        
response_code  = 0      
while response_code != -1:
    response_code = int(input ("Enter An HTTP response code? "))
    http_response = hppt(response_code)
    print (f"Page Request returned {response_code} : {http_response}")