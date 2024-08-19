#break statement is used to break out of a given for or while loop

for i in range(2,10):
    for j in range(2,i):
        if i%j == 0:
            print(f"{i} is Not a prime number")
            break
    else: #this else statement is executed only after the inner for loop iterable is exhausted, i.e when no break occurs.
        print(f"{i} is a Prime number")