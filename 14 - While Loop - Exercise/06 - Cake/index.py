width = int(input())
height = int(input())

cake_pieces = width * height

while True:
    value = input()

    if value == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break

    cake_pieces -= int(value)

    if cake_pieces <= 0:
        difference = abs(cake_pieces)
        print(f"No more cake left! You need {difference} pieces more.")
        break