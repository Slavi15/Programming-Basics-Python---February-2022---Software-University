dyed_eggs_count = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

max_eggs_count = 0
max_eggs_name = ""

for i in range(0, dyed_eggs_count):
    colour = str(input())

    if i == 0:
        max_eggs_count += 1

    if colour == "red":
        red_eggs += 1
        if red_eggs > max_eggs_count:
            max_eggs_count = red_eggs
            max_eggs_name = "red"
    elif colour == "orange":
        orange_eggs += 1
        if orange_eggs > max_eggs_count:
            max_eggs_count = orange_eggs
            max_eggs_name = "orange"
    elif colour == "blue":
        blue_eggs += 1
        if blue_eggs > max_eggs_count:
            max_eggs_count = blue_eggs
            max_eggs_name = "blue"
    elif colour == "green":
        green_eggs += 1
        if green_eggs > max_eggs_count:
            max_eggs_count = green_eggs
            max_eggs_name = "green"

print(f"""Red eggs: {red_eggs}
Orange eggs: {orange_eggs}
Blue eggs: {blue_eggs}
Green eggs: {green_eggs}
Max eggs: {max_eggs_count} -> {max_eggs_name}""")