import math

days_count = int(input())
left_food_kg = int(input())
food_per_day_dog = float(input())
food_per_day_cat = float(input())
food_per_day_turtle = float(input()) / 1000

needed_food_dog = food_per_day_dog * days_count
needed_food_cat = food_per_day_cat * days_count
needed_food_turtle = food_per_day_turtle * days_count

all_food = needed_food_dog + needed_food_cat + needed_food_turtle
left_food = abs(all_food - left_food_kg)

if left_food_kg >= all_food:
    print(f"{math.floor(left_food)} kilos of food left.")
else:
    print(f"{math.ceil(left_food)} more kilos of food are needed.")