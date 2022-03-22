start_amount_eggs = int(input())

sold_eggs = 0

while True:
    value = str(input())

    if value == "Close":
        print(f"""Store is closed!
        {sold_eggs} eggs sold.""")
        break

    eggs_count = int(input())

    if value == "Buy":
        if (start_amount_eggs - eggs_count) < 0:
            print(f"""Not enough eggs in store!
            You can buy only {start_amount_eggs}.""")
            break
        
        start_amount_eggs -= eggs_count
        sold_eggs += eggs_count
    elif value == "Fill":
        start_amount_eggs += eggs_count