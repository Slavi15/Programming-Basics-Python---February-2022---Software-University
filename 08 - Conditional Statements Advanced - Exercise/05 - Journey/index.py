budget = float(input())
season = str(input())

price = 0
holiday_type = ""

if budget <= 100:
    if season == "summer":
        holiday_type = "Camp"
        price = budget * 0.3
    elif season == "winter":
        holiday_type = "Hotel"
        price = budget * 0.7
    print(f"Somewhere in Bulgaria")
    print(f"{holiday_type} - {price:.2f}")
elif budget > 100 and budget <= 1000:
    if season == "summer":
        holiday_type = "Camp"
        price = budget * 0.4
    elif season == "winter":
        holiday_type = "Hotel"
        price = budget * 0.8
    print(f"Somewhere in Balkans")
    print(f"{holiday_type} - {price:.2f}")
elif budget > 1000:
    holiday_type = "Hotel"
    price = budget * 0.9
    print(f"Somewhere in Europe")
    print(f"{holiday_type} - {price:.2f}")