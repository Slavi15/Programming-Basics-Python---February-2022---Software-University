available_money = float(input())
sex_type = str(input())
age = int(input())
sports_type = str(input())

needed_money = 0

if sex_type == "m":
    if sports_type == "Gym":
        needed_money = 42
    elif sports_type == "Boxing":
        needed_money = 41
    elif sports_type == "Yoga":
        needed_money = 45
    elif sports_type == "Zumba":
        needed_money = 34
    elif sports_type == "Dances":
        needed_money = 51
    elif sports_type == "Pilates":
        needed_money = 39
elif sex_type == "f":
    if sports_type == "Gym":
        needed_money = 35
    elif sports_type == "Boxing":
        needed_money = 37
    elif sports_type == "Yoga":
        needed_money = 42
    elif sports_type == "Zumba":
        needed_money = 31
    elif sports_type == "Dances":
        needed_money = 53
    elif sports_type == "Pilates":
        needed_money = 37

if age <= 19:
    needed_money -= (needed_money * 0.2)

if available_money >= needed_money:
    print(f"You purchased a 1 month pass for {sports_type}.")
else:
    diff = abs(available_money - needed_money)
    print(f"You don't have enough money! You need ${diff:.2f} more.")