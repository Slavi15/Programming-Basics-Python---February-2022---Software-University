budget = int(input())
season = str(input())
fishers_count = int(input())

ship_rent = 0
price = 0

if season == "Spring":
    ship_rent = 3000
    price += ship_rent
    if fishers_count <= 6:
        price -= (price * 0.1)
    elif fishers_count >= 7 and fishers_count <= 11:
        price -= (price * 0.15)
    elif fishers_count >= 12:
        price -= (price * 0.25)
elif season == "Summer":
    ship_rent = 4200
    price += ship_rent
    if fishers_count <= 6:
        price -= (price * 0.1)
    elif fishers_count >= 7 and fishers_count <= 11:
        price -= (price * 0.15)
    elif fishers_count >= 12:
        price -= (price * 0.25)
elif season == "Autumn":
    ship_rent = 4200
    price += ship_rent
    if fishers_count <= 6:
        price -= (price * 0.1)
    elif fishers_count >= 7 and fishers_count <= 11:
        price -= (price * 0.15)
    elif fishers_count >= 12:
        price -= (price * 0.25)
elif season == "Winter":
    ship_rent = 2600
    price += ship_rent
    if fishers_count <= 6:
        price -= (price * 0.1)
    elif fishers_count >= 7 and fishers_count <= 11:
        price -= (price * 0.15)
    elif fishers_count >= 12:
        price -= (price * 0.25)

if fishers_count % 2 == 0 and season != "Autumn":
    price -= (price * 0.05)

left_money = abs(price - budget)
if price <= budget:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")