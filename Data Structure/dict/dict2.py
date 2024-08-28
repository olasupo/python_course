#Example - Looping through a dict
phonebook = {
    "Kunle" : "+1 742 2340 789",
    "Smart" : "+234 904 5690 532",
    "Rishi" : "+44 798 4322 786",
}

eyan = "James"

for name in phonebook.keys():
    if eyan in phonebook.keys():
        print(f"{eyan} wa")
        break
else:
    print("Not found")
for number in phonebook.values():
    print(number)

for name, number in phonebook.items():
    print(f"Name: {name} : Number  {number}")
  
