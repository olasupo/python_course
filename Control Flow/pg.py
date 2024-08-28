#Example - Looping through a dict
phonebook =[
     {"Name" : "Kunle", "Phone": "+1 742 2340 789"},
     {"Name" : "Smart", "Phone" : "+234 904 5690 532"},
     {"Name": "Rishi", "Phone" : "+44 798 4322 786"},
]

phonebook1 =[
     { "Kunle": "+1 742 2340 789"},
     { "Smart" : "+234 904 5690 532"},
     {"Rishi" : "+44 798 4322 786"},
]


person1 ={"Name" : "Kunle", "Phone": "+1 742 2340 789"}
person2 =  {"Name" : "Smart", "Phone" : "+234 904 5690 532"}
person3 = {"Name": "Rishi", "Phone" : "+44 798 4322 786"}

searchForPerson = input("Enter name to search for: ")

print(person1["Name"])
print(phonebook1[0])

if searchForPerson in phonebook1:
    print ("Hurray")


for ls in phonebook1:
    for  keys in ls:
        if  searchForPerson in keys:
            print(f"{searchForPerson} found in phonebook1")
        

for ls in phonebook:
    for values in ls.values():
        if searchForPerson in values:
            print(f"{searchForPerson} found in phonebook too")

  
