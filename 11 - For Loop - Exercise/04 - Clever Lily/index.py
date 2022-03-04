age = int(input())
washer_price = float(input())
toy_price_per_one = int(input())

toy_count = 0
money = 0
received_money = 10

for i in range(1, age + 1):
    if i % 2 == 0:
        money += received_money
        money -= 1
        received_money += 10
    elif i % 2 != 0:
        toy_count += 1

toy_price = toy_price_per_one * toy_count
money += toy_price

diff = abs(money - washer_price)
if money >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")