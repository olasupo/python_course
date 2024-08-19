#Iterate over a list using range

names = ["Dammy", "Gareth", "Suzie"]

for i in range(len(names)):
    print(f"index {i} is {names[i]}")

for b in enumerate(names):
    print (b)
    if "Suzie" in b:
        print("Hurray")
