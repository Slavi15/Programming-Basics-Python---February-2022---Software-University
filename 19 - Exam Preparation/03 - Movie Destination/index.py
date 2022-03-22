budget_money = float(input())
destination = str(input())
season = str(input())
days_count = int(input())

money = 0

if season == "Summer":
    if destination == "Dubai":
        money = days_count * 40000
        money -= (money * 0.3)
    elif destination == "Sofia":
        money = days_count * 12500
        money += (money * 0.25)
    elif destination == "London":
        money = days_count * 20250
elif season == "Winter":
    if destination == "Dubai":
        money = days_count * 45000
        money -= (money * 0.3)
    elif destination == "Sofia":
        money = days_count * 17000
        money += (money * 0.25)
    elif destination == "London":
        money = days_count * 24000

diff = abs(budget_money - money)
if budget_money >= money:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")