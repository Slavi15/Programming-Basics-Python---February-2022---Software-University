desired_income = float(input())

money = 0

while True:
    cocktail_name = str(input())

    if cocktail_name == "Party!":
        diff = abs(desired_income - money)
        print(f"We need {diff:.2f} leva more.")
        break

    coktails_count = int(input())
    cocktail_price = len(cocktail_name)
    order_price = coktails_count * cocktail_price

    if order_price % 2 != 0:
        order_price -= (order_price * 0.25)
    
    money += order_price

    if money >= desired_income:
        print("Target acquired.")
        break

print(f"Club income - {money:.2f} leva.")