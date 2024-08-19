#Iterating through a dictionary
person = {"fname":"Olasupo","lname":"Okunaiya","age":39, "height": "1.7m"}
placeholder=[]

for key, value in person.items():
    print(key, value)
    if key == "lname":
        continue
        print("We will NOT stop here")
        
    elif value == 39:
        person[key] = value + 10
        print(f"He is {value} years old")
        break
print (person)



