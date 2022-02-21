import math

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cacti_count = int(input())
present_price = float(input())

magnolia_price = magnolia_count * 3.25
hyacinth_price = hyacinth_count * 4
rose_price = rose_count * 3.5
cacti_price = cacti_count * 8

price_without_tax = magnolia_price + hyacinth_price + rose_price + cacti_price
price = price_without_tax - (price_without_tax * 0.05)

left_money = abs(price - present_price)

if price >= present_price:
    print(f"She is left with {math.floor(left_money)} leva." )
else:
    print(f"She will have to borrow {math.ceil(left_money)} leva." )