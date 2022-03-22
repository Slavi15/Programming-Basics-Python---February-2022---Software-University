t_shirt_price = float(input())
needed_money_prize = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (shorts_price + t_shirt_price) * 2

pepi_money = t_shirt_price + shorts_price + socks_price + shoes_price
pepi_money -= (pepi_money * 0.15)

if pepi_money >= needed_money_prize:
    print(f"""Yes, he will earn the world-cup replica ball!
    His sum is {pepi_money:.2f} lv.""")
else:
    needed_money = abs(pepi_money - needed_money_prize)
    print(f"""No, he will not earn the world-cup replica ball.
    He needs {needed_money:.2f} lv. more.""")