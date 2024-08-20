def tribe(response):
    match response:
        case a if response in range(0,2):
            return "Baby"
        case b if response in range(2,6):
            return "Toddler"
        case c if response in range(6,13):
            return "Adolescent"
        case d if response in range(13,20):
            return "Teenager"
        case e if response >=20 and response <=100:
            return "Adult"
        case _:
            return "Not Likely a valid value"
        
        
response=0
while response != -1:
    response = int(input ("Please input your age? "))
    age_group = tribe(response)
    print (f"You are in the {age_group} age group")