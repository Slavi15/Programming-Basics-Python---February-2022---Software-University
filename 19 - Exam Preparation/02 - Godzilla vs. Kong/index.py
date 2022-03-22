budget_money = float(input())
statists_count = int(input())
clothes_statist_price = float(input())

decor_price = budget_money * 0.1

if statists_count > 150:
    clothes_statist_price -= (clothes_statist_price * 0.1)

statists_money = statists_count * clothes_statist_price

all_money = decor_price + statists_money

diff = abs(budget_money - all_money)
if budget_money >= all_money:
    print(f"""Action!
    Wingard starts filming with {diff:.2f} leva left.""")
else:
    print(f"""Not enough money!
    Wingard needs {diff:.2f} leva more.""")