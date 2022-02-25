days = int(input())
room_type = str(input())
mark = str(input())

nights = days - 1
price = 0

if room_type == "room for one person":
    price = nights * 18
elif room_type == "apartment":
    price = nights * 25
    if days < 10:
        price -= (price * 0.3)
    elif days >= 10 and days <= 15:
        price -= (price * 0.35)
    elif days > 15:
        price -= (price * 0.5)
elif room_type == "president apartment":
    price = nights * 35
    if days < 10:
        price -= (price * 0.1)
    elif days >= 10 and days <= 15:
        price -= (price * 0.15)
    elif days > 15:
        price -= (price * 0.2)

if mark == "positive":
    price += (price * 0.25)
elif mark == "negative":
    price -= (price * 0.1)

print(f"{price:.2f}")