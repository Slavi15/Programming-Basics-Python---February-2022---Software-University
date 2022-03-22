room_rent = float(input())

cake_price = room_rent * 0.2
drinks_price = cake_price - (cake_price * 0.45)
animator_price = room_rent / 3

needed_budget = room_rent + cake_price + drinks_price + animator_price
print(needed_budget)