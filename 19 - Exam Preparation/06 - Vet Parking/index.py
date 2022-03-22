days_count = int(input())
hours_count = int(input())

total_money = 0
money = 0

for day in range(1, days_count + 1):
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_money += 2.5
            money += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            total_money += 1.25
            money += 1.25
        else:
            total_money += 1
            money += 1
    print(f"Day: {day} - {money:.2f} leva")
    money = 0

print(f"Total: {total_money:.2f} leva")