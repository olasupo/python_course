#break statement is used to break out of a given for or while loop

print()
for i in range(2,10):
        if i%2 == 0:
            print(f"{i} is an Even number")
            continue
        print (f"{i} is an Odd number.")
    