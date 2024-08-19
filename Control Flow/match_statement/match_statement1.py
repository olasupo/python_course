def tribe(geolo):
    match geolo:
        case "west" | "West":
            return "Yoruba"
        case "east" | "East":
            return "Igbo"
        case "north" | "North":
            return "Hausa"
        


while True:
    response = input ("What part of the country are you from? ")
    your_tribe = tribe(response)
    print (f"You are of the {your_tribe} tribe")