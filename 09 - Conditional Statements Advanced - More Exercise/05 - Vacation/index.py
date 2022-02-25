budget = float(input())
season = str(input())

living_place = ""
place = ""
price = 0

if budget <= 1000:
    living_place = "Camp"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.45
elif budget > 1000 and budget <= 3000:
    living_place = "Hut"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.6
elif budget > 3000:
    living_place = "Hotel"
    if season == "Summer":
        place = "Alaska"
    elif season == "Winter":
        place = "Morocco"
    price = budget * 0.9

print(f"{place} - {living_place} - {price:.2f}")