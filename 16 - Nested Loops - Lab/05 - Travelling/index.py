all_money = 0

while True:
    destination = str(input())
    
    if destination == "End":
        break

    needed_money = float(input())

    while True:
        money = float(input())
        all_money += money

        if all_money >= needed_money:
            print(f"Going to {destination}!")
            all_money = 0
            break