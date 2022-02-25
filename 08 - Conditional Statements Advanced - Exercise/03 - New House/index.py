flowers_type = str(input())
flowers_count = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

price = 0

if flowers_type == "Roses":
    price = flowers_count * rose_price
    if flowers_count > 80:
        price -= (price * 0.1)
elif flowers_type == "Dahlias":
    price = flowers_count * dahlia_price
    if flowers_count > 90:
        price -= (price * 0.15)
elif flowers_type == "Tulips":
    price = flowers_count * tulip_price
    if flowers_count > 80:
        price -= (price * 0.15)
elif flowers_type == "Narcissus":
    price = flowers_count * narcissus_price
    if flowers_count < 120:
        price += (price * 0.15)
elif flowers_type == "Gladiolus":
    price = flowers_count * gladiolus_price
    if flowers_count < 80:
        price += (price * 0.2)

left_money = abs(price - budget)
if price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {left_money:.2f} leva left.")
elif price > budget:
    print(f"Not enough money, you need {left_money:.2f} leva more.")