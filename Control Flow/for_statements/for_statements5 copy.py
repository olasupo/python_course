#Iterating through a string
name = "Peter"
placeholder=[]

for char in name:
    j= name.index(char)
    #print (f"{char} is in the name {name}")
    placeholder.append(char)
    print (placeholder, end="")
    if placeholder.count(char) > 1:
        pc=placeholder.count(char)
        print(f"{char} has occured {pc} times")
        break
    if len(placeholder) > 2:
        print(f"length of placeholder is {len(placeholder)}")
        break


