room_capacity = int(input())

money = 0
taken_seats = 0

while True:
    value = input()

    if value == "Movie time!":
        diff = abs(room_capacity - taken_seats)
        print(f"There are {diff} seats left in the cinema.")
        break
    
    taken_seats += int(value)
    if taken_seats > room_capacity:
        print(f"The cinema is full.")
        break

    money += (int(value) * 5)

    if int(value) % 3 == 0:
        money -= 5

print(f"Cinema income - {money} lv.")