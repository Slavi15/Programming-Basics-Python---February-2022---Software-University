strawberry_price = float(input())
banana_amount_kg = float(input())
orange_amount_kg = float(input())
raspberry_amount_kg = float(input())
strawberry_amount_kg = float(input())

strawberries = strawberry_price * strawberry_amount_kg

raspberry_price = strawberry_price / 2
raspberries = raspberry_price * raspberry_amount_kg

orange_price = raspberry_price - (raspberry_price * 0.4)
oranges = orange_price * orange_amount_kg

banana_price = raspberry_price - (raspberry_price * 0.8)
bananas = banana_price * banana_amount_kg

money = strawberries + raspberries + oranges + bananas
print(f"{money:.2f}")