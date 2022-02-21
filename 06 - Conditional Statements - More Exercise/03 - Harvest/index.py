import math

valley_square_meters = int(input())
grapes_per_square_meter = float(input())
wine_needed_litres = int(input())
workers_count = int(input())

all_grapes = valley_square_meters * grapes_per_square_meter
wine = (all_grapes * 0.4) / 2.5

needed_wine = abs(wine - wine_needed_litres)

if wine < wine_needed_litres:
    print(f"It will be a tough winter! More {math.floor(needed_wine)} liters wine needed.")
elif wine >= wine_needed_litres:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(needed_wine)} liters left -> {math.ceil(needed_wine / workers_count)} liters per person.")