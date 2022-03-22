people_count = int(input())
season = str(input())

money = 0

if season == "spring":
    if people_count <= 5:
        money = people_count * 50
    elif people_count > 5:
        money = people_count * 48
elif season == "summer":
    if people_count <= 5:
        money = people_count * 48.5
    elif people_count > 5:
        money = people_count * 45

    money -= (money * 0.15)
elif season == "autumn":
    if people_count <= 5:
        money = people_count * 60
    elif people_count > 5:
        money = people_count * 49.5
elif season == "winter":
    if people_count <= 5:
        money = people_count * 86
    elif people_count > 5:
        money = people_count * 85

    money += (money * 0.08)

print(f"{money:.2f} leva.")