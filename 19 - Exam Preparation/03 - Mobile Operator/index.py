contract_deadline = str(input())
contract_type = str(input())
mobile_data = str(input())
months_for_pay = int(input())

money = 0

if contract_deadline == "one":
    if contract_type == "Small":
        money += 9.98
    elif contract_type == "Middle":
        money += 18.99
    elif contract_type == "Large":
        money += 25.98
    elif contract_type == "ExtraLarge":
        money += 35.99
elif contract_deadline == "two":
    if contract_type == "Small":
        money += 8.58
    elif contract_type == "Middle":
        money += 17.09
    elif contract_type == "Large":
        money += 23.59
    elif contract_type == "ExtraLarge":
        money += 31.79

if mobile_data == "yes":
    if money <= 10:
        money += 5.5
    elif money <= 30 and money > 10:
        money += 4.35
    elif money > 30:
        money += 3.85

if contract_deadline == "two":
    money -= (money * 0.0375)

money *= months_for_pay
print(f"{money:.2f} lv.")