vacation_money = float(input())
available_money = float(input())

money = available_money
spend_action_count = 0
days_count = 0

while True:
    action = str(input())
    amount_of_money = float(input())

    days_count += 1

    if action == "spend":
        spend_action_count += 1
        money -= amount_of_money
        if money < 0:
            money = 0
    elif action == "save":
        spend_action_count = 0
        money += amount_of_money

    if spend_action_count == 5:
        print(f"""You can't save the money.
        {days_count}""")
        break

    if money >= vacation_money:
        print(f"You saved the money for {days_count} days.")
        break