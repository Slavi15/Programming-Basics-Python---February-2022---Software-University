budget = float(input())
season = str(input())

car_class = ""
car_type = ""
car_price = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        car_price = budget * 0.65
elif budget > 100 and budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        car_price = budget * 0.8
elif budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    car_price = budget * 0.9

print(f"""{car_class}
{car_type} - {car_price:.2f}""")