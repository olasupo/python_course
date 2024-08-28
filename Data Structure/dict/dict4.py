#Example - Looping through a dict
phonebook =[
     {"Name" : "Kunle", "Phone": "+1 742 2340 789"},
     {"Name" : "Smart", "Phone" : "+234 904 5690 532"},
     {"Name": "Rishi", "Phone" : "+44 798 4322 786"},
]

searchForPerson = input("Enter name to search for: ")

for person in phonebook:
    for values in person.values():
        if searchForPerson in values:
            print(f" {searchForPerson} found in the phonebook")
            break
else:
        print (f"{searchForPerson} not found")    
    







  
