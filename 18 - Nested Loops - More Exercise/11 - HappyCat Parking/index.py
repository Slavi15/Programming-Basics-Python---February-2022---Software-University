days_count = int(input())
hours_per_day = int(input())

all_money = 0

for day in range(1, days_count + 1):
    price = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price += 2.5
            all_money += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price += 1.25
            all_money += 1.25
        else:
            price += 1
            all_money += 1
    print(f"Day: {day} - {price:.2f} leva")

print(f"Total: {all_money:.2f} leva")