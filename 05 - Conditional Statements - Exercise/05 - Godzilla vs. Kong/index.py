film_budget = float(input())
statist_count = int(input())
clothes_statist_price = float(input())

decor_price = film_budget * 0.1
clothes_price = statist_count * clothes_statist_price

if statist_count > 150:
    clothes_price -= (clothes_price * 0.1)

money = decor_price + clothes_price
needed_money = abs(money - film_budget)

if money > film_budget:
    print(f"Not enough money!\nWingard needs {needed_money:.2f} leva more.")
elif money <= film_budget:
    print(f"Action!\nWingard starts filming with {needed_money:.2f} leva left.")