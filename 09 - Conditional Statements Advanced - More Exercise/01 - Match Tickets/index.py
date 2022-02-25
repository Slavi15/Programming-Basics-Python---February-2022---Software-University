budget = float(input())
category = str(input())
people_count = int(input())

vip_price = 499.99
normal_price = 249.99

transport_money = 0

if people_count >= 1 and people_count <= 4:
    transport_money = budget * 0.75
elif people_count >= 5 and people_count <= 9:
    transport_money = budget * 0.6
elif people_count >= 10 and people_count <= 24:
    transport_money = budget * 0.5
elif people_count >= 25 and people_count <= 49:
    transport_money = budget * 0.4
elif people_count >= 50:
    transport_money = budget * 0.25

money_without_transport = budget - transport_money
if category == "VIP":
    ticket_money = people_count * vip_price
elif category == "Normal":
    ticket_money = people_count * normal_price

left_money = abs(ticket_money - money_without_transport)
if money_without_transport >= ticket_money:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")