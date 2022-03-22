budget_money = float(input())
nights_count = int(input())
one_night_price = float(input())
percent_additional_tax = int(input())

if nights_count > 7:
    one_night_price -= (one_night_price * 0.05)

money_for_nights = nights_count * one_night_price
additional_taxes = (budget_money * percent_additional_tax) / 100

money = money_for_nights + additional_taxes

diff = abs(budget_money - money)
if budget_money >= money:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")