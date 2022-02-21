fuel_type = str(input())
fuel_litres = float(input())
vip_card = str(input())

price = 0

if fuel_type == "Diesel":
    if vip_card == "Yes":
        price = fuel_litres * 2.21
    elif vip_card == "No":
        price = fuel_litres * 2.33
elif fuel_type == "Gas":
    if vip_card == "Yes":
        price = fuel_litres * 0.85
    elif vip_card == "No":
        price = fuel_litres * 0.93
elif fuel_type == "Gasoline":
    if vip_card == "Yes":
        price = fuel_litres * 2.04
    elif vip_card == "No":
        price = fuel_litres * 2.22

if fuel_litres >= 20 and fuel_litres <= 25:
    price -= (price * 0.08)
elif fuel_litres > 25:
    price -= (price * 0.1)

print(f"{price:.2f} lv.")