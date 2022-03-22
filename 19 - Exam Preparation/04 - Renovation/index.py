import math

height = int(input())
width = int(input())
percent_not_painted = int(input())

all_walls = height * width * 4
walls_to_be_painted = math.ceil(all_walls - (all_walls * (percent_not_painted / 100)))

while True:
    value = input()
    if value == "Tired!":
        print(f"{walls_to_be_painted} quadratic m left.")
        break

    walls_to_be_painted -= int(value)

    if walls_to_be_painted < 0:
        print(f"All walls are painted and you have {abs(walls_to_be_painted)} l paint left!")
        break
    if walls_to_be_painted == 0:
        print("All walls are painted! Great job, Pesho!")
        break