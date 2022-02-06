needed_amount_nylon = int(input())
needed_amount_paint = int(input())
diluent_amount_litres = int(input())
hours = int(input())

nylon_price = 1.5
paint_price = 14.5
diluent_price = 5

paint_amount = needed_amount_paint + (needed_amount_paint * 0.1)
nylon_amount = needed_amount_nylon + 2

price_materials = (paint_amount * paint_price) + (nylon_amount * nylon_price) + (diluent_amount_litres * diluent_price) + 0.4
price_for_hour = price_materials * 0.3
price_for_builders = price_for_hour * hours

price = price_materials + price_for_builders

print(price)