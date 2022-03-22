kozunaks_number = int(input())

points = 0
highest_result = 0
best_cook = ""

for i in range(0, kozunaks_number):
    name = str(input())

    while True:
        value = input()

        if value == "Stop":
            print(f"{name} has {points} points.")
            if points == highest_result:
                print(f"{name} is the new number 1!")
            break

        points += int(value)

        if points > highest_result:
            highest_result = points
            best_cook = name

    points = 0

print(f"{best_cook} won competition with {highest_result} points!")