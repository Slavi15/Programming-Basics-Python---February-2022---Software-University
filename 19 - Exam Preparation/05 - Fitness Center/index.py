customers_count = int(input())

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake = 0
protein_bar = 0

workout_people = 0
protein_people = 0

for i in range(0, customers_count):
    activity = str(input())

    if activity == "Back":
        back_count += 1
        workout_people += 1
    elif activity == "Chest":
        chest_count += 1
        workout_people += 1
    elif activity == "Legs":
        legs_count += 1
        workout_people += 1
    elif activity == "Abs":
        abs_count += 1
        workout_people += 1
    elif activity == "Protein shake":
        protein_shake += 1
        protein_people += 1
    elif activity == "Protein bar":
        protein_bar += 1
        protein_people += 1

p1 = (workout_people / customers_count) * 100
p2 = (protein_people / customers_count) * 100
print(f"""{back_count} - back
{chest_count} - chest
{legs_count} - legs
{abs_count} - abs
{protein_shake} - protein shake
{protein_bar} - protein bar
{p1:.2f}% - work out
{p2:.2f}% - protein""")