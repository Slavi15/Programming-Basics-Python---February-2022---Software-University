bought_amount_food = int(input())

food_grams = bought_amount_food * 1000
eaten_food_dog = 0

while True:
    value = input()

    if value == "Adopted":
        break
    else:
        eaten_food_dog += int(value)

diff = abs(food_grams - eaten_food_dog)
if food_grams >= eaten_food_dog:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more." )