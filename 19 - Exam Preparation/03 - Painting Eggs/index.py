eggs_size = str(input())
eggs_colour = str(input())
partides_count = int(input())

income = 0

if eggs_size == "Large":
    if eggs_colour == "Red":
        income = partides_count * 16
    elif eggs_colour == "Green":
        income = partides_count * 12
    elif eggs_colour == "Yellow":
        income = partides_count * 9
elif eggs_size == "Medium":
    if eggs_colour == "Red":
        income = partides_count * 13
    elif eggs_colour == "Green":
        income = partides_count * 9
    elif eggs_colour == "Yellow":
        income = partides_count * 7
elif eggs_size == "Small":
    if eggs_colour == "Red":
        income = partides_count * 9
    elif eggs_colour == "Green":
        income = partides_count * 8
    elif eggs_colour == "Yellow":
        income = partides_count * 5

income -= (income * 0.35)
print(f"{income:.2f} leva.")