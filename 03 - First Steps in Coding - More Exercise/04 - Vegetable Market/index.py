vegetable_price_per_kg = float(input())
fruit_price_per_kg = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

price_leva = (vegetable_price_per_kg * vegetable_kg) + (fruit_price_per_kg * fruit_kg)
price_euro = price_leva / 1.94
print(f"{price_euro:.2f}")