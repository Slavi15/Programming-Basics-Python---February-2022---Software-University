holiday_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = 2.6
doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
truck_price = 2

toys_count = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count
price = (puzzle_count * puzzle_price) + (doll_count * doll_price) + (teddy_bear_count * teddy_bear_price) + (minion_count * minion_price) + (truck_count * truck_price)

if toys_count >= 50:
    price -= (price * 0.25)

price -= (price * 0.1)

left_money = abs(price - holiday_price)

if price >= holiday_price:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")