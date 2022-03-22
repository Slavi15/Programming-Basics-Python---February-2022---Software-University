minutes_per_day = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

all_walks_minutes = minutes_per_day * walks_per_day
burnt_calories = all_walks_minutes * 5

if burnt_calories >= (calories_per_day / 2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.")