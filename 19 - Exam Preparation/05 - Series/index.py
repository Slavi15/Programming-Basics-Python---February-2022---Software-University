budget_money = float(input())
series_count = int(input())

price = 0

for i in range(0, series_count):
    series_name = str(input())
    series_price = float(input())

    if series_name == "Thrones":
        series_price -= (series_price * 0.5)
        price += series_price
    elif series_name == "Lucifer":
        series_price -= (series_price * 0.4)
        price += series_price
    elif series_name == "Protector":
        series_price -= (series_price * 0.3)
        price += series_price
    elif series_name == "TotalDrama":
        series_price -= (series_price * 0.2)
        price += series_price
    elif series_name == "Area":
        series_price -= (series_price * 0.1)
        price += series_price
    else:
        price += series_price

diff = abs(budget_money - price)
if budget_money >= price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")