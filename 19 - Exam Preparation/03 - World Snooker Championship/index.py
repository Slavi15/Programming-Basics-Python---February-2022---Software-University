championship_phase = str(input())
ticket_type = str(input())
tickets_count = int(input())
image_with_trophy = str(input())

money = 0

if championship_phase == "Quarter final":
    if ticket_type == "Standard":
        money = tickets_count * 55.5
    elif ticket_type == "Premium":
        money = tickets_count * 105.2
    elif ticket_type == "VIP":
        money = tickets_count * 118.9
elif championship_phase == "Semi final":
    if ticket_type == "Standard":
        money = tickets_count * 75.88
    elif ticket_type == "Premium":
        money = tickets_count * 125.22
    elif ticket_type == "VIP":
        money = tickets_count * 300.4
elif championship_phase == "Final":
    if ticket_type == "Standard":
        money = tickets_count * 110.1
    elif ticket_type == "Premium":
        money = tickets_count * 160.66
    elif ticket_type == "VIP":
        money = tickets_count * 400

if money > 4000:
    money -= (money * 0.25)
elif money > 2500 and money <= 4000:
    money -= (money * 0.1)
    if image_with_trophy == "Y":
        money += (tickets_count * 40)
elif money <= 2500:
    if image_with_trophy == "Y":
        money += (tickets_count * 40)

print(f"{money:.2f}")