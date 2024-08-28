#Example - Looping through a dict
phonebook =[
     {"Name" : "Kunle", "Phone": "+1 742 2340 789"},
     {"Name" : "Smart", "Phone" : "+234 904 5690 532"},
     {"Name": "Rishi", "Phone" : "+44 798 4322 786"},
]

for person in phonebook:
    print(person["Name"])

for number in phonebook:
    print(number["Phone"])



  
