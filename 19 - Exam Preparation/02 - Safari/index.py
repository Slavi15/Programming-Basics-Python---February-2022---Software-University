budget_money = float(input())
needed_petrol_litres = float(input())
day_of_week = str(input())

litre_petrol_price = 2.1
tour_guide_price = 100

petrol = needed_petrol_litres * litre_petrol_price
money = petrol + tour_guide_price

if day_of_week == "Saturday":
    money -= (money * 0.1)
elif day_of_week == "Sunday":
    money -= (money * 0.2)

diff = abs(budget_money - money)
if budget_money >= money:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")