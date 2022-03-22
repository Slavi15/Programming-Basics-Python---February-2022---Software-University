days_count = int(input())
all_amount_food = float(input())

total_biscuits_amount = 0
eaten_dog_food = 0
eaten_cat_food = 0

for i in range(1, days_count + 1):
    food_for_day_dog = int(input())
    food_for_day_cat = int(input())

    eaten_dog_food += food_for_day_dog
    eaten_cat_food += food_for_day_cat

    if i % 3 == 0:
        food_for_day = food_for_day_dog + food_for_day_cat
        total_biscuits_amount += (food_for_day * 0.1)

all_eaten_food = eaten_dog_food + eaten_cat_food
percent_of_food_eaten = (all_eaten_food / all_amount_food) * 100
percent_of_food_dog = (eaten_dog_food / all_eaten_food) * 100
percent_of_food_cat = (eaten_cat_food / all_eaten_food) * 100

print(f"""Total eaten biscuits: {round(total_biscuits_amount)}gr.
{percent_of_food_eaten:.2f}% of the food has been eaten.
{percent_of_food_dog:.2f}% eaten from the dog.
{percent_of_food_cat:.2f}% eaten from the cat.""")