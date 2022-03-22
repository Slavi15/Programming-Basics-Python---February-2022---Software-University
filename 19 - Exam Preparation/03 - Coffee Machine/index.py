drink_type = str(input())
sugar = str(input())
drinks_count = int(input())

money = 0

if sugar == "Without":
    if drink_type == "Espresso":
        money = drinks_count * 0.9
        money -= (money * 0.35)
        if drinks_count >= 5:
            money -= (money * 0.25)
    elif drink_type == "Cappuccino":
        money = drinks_count * 1
        money -= (money * 0.35)
    elif drink_type == "Tea":
        money = drinks_count * 0.5
        money -= (money * 0.35)
elif sugar == "Normal":
    if drink_type == "Espresso":
        money = drinks_count * 1
        if drinks_count >= 5:
            money -= (money * 0.25)
    elif drink_type == "Cappuccino":
        money = drinks_count * 1.2
    elif drink_type == "Tea":
        money = drinks_count * 0.6
elif sugar == "Extra":
    if drink_type == "Espresso":
        money = drinks_count * 1.2
        if drinks_count >= 5:
            money -= (money * 0.25)
    elif drink_type == "Cappuccino":
        money = drinks_count * 1.6
    elif drink_type == "Tea":
        money = drinks_count * 0.7

if money > 15:
    money -= (money * 0.2)

print(f"You bought {drinks_count} cups of {drink_type} for {money:.2f} lv.")