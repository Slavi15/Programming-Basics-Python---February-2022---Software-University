budget_money = float(input())

products_count = 0
money = 0

while True:
    text = str(input())

    if text == "Stop":
        print(f"You bought {products_count} products for {money:.2f} leva.")
        break

    product_price = float(input())
    products_count += 1

    if products_count % 3 == 0:
        product_price /= 2

    budget_money -= product_price

    if budget_money < 0:
        print(f"""You don't have enough money!
        You need {abs(budget_money):.2f} leva!""")
        break
    else:
        money += product_price