town_name = str(input())
packet_type = str(input())
vip_discount = str(input())
days_count = int(input())

money = 0

if town_name == "Bansko" or town_name == "Borovets":
    if packet_type == "withEquipment":
        if days_count < 1:
            print("Days must be positive number!")
        else:
            money = days_count * 100

            if days_count > 7:
                money -= 100

            if vip_discount == "yes":
                money -= (money * 0.1)

            print(f"The price is {money:.2f}lv! Have a nice time!")
    elif packet_type == "noEquipment":
        if days_count < 1:
            print("Days must be positive number!")
        else:
            money = days_count * 80

            if days_count > 7:
                money -= 80

            if vip_discount == "yes":
                money -= (money * 0.05)

            print(f"The price is {money:.2f}lv! Have a nice time!")
    else:
        print("Invalid input!")
elif town_name == "Varna" or town_name == "Burgas":
    if packet_type == "withBreakfast":
        if days_count < 1:
            print("Days must be positive number!")
        else:
            money = days_count * 130

            if days_count > 7:
                money -= 130

            if vip_discount == "yes":
                money -= (money * 0.12)

            print(f"The price is {money:.2f}lv! Have a nice time!")
    elif packet_type == "noBreakfast":
        if days_count < 1:
            print("Days must be positive number!")
        else:
            money = days_count * 100

            if days_count > 7:
                money -= 100

            if vip_discount == "yes":
                money -= (money * 0.07)

            print(f"The price is {money:.2f}lv! Have a nice time!")
    else:
        print("Invalid input!")
else:
    print("Invalid input!")