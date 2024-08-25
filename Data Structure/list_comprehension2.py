#Example - using list comprehensions
a = [1,5,2]

b = [1,4,6]

[a.extend(b) for i in range(1) if a != b]

print(a)

