celsius = int(input())
time_of_day = input()

outfit = ""
shoes = ""

if time_of_day == "Morning":
    if celsius >= 10 and celsius <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif celsius > 18 and celsius <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif celsius >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if celsius >= 10 and celsius <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif celsius > 18 and celsius <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif celsius >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time_of_day == "Evening":
    if celsius >= 10 and celsius <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif celsius > 18 and celsius <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif celsius >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {celsius} degrees, get your {outfit} and {shoes}.")