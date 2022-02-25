season = str(input())
group_type = str(input())
students = int(input())
nights = int(input())

price = 0
girls_sport = ""
boys_sport = ""
mixed_sport = ""

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price = students * nights * 9.6
    elif group_type == "mixed":
        price = students * nights * 10

    boys_sport = "Judo"
    girls_sport = "Gymnastics"
    mixed_sport = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price = students * nights * 7.2
    elif group_type == "mixed":
        price = students * nights * 9.5

    boys_sport = "Tennis"
    girls_sport = "Athletics"
    mixed_sport = "Cycling"
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price = students * nights * 15
    elif group_type == "mixed":
        price = students * nights * 20

    boys_sport = "Football"
    girls_sport = "Volleyball"
    mixed_sport = "Swimming"

if students >= 50:
    price -= (price * 0.5)
elif students >= 20 and students < 50:
    price -= (price * 0.15)
elif students >= 10 and students < 20:
    price -= (price * 0.05)

if group_type == "boys":
    print(f"{boys_sport} {price:.2f} lv.")
elif group_type == "girls":
    print(f"{girls_sport} {price:.2f} lv.")
elif group_type == "mixed":
    print(f"{mixed_sport} {price:.2f} lv.")