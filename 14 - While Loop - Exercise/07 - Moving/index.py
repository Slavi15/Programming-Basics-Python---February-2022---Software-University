width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
available_volume = volume

while True:
    value = input()

    if value == "Done" and volume > 0:
        print(f"{available_volume} Cubic meters left.")
        break

    available_volume -= int(value)

    if available_volume <= 0:
        diff = abs(available_volume)
        print(f"No more free space! You need {diff} Cubic meters more.")
        break