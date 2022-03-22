voucher_money = int(input())

purchase_price = 0
tickets_count = 0
others = 0

while True:
    value = str(input())
    
    if value == "End":
        break

    if len(value) > 8:
        purchase_price = ord(value[0]) + ord(value[1])
        if voucher_money >= purchase_price:
            tickets_count += 1
            voucher_money -= purchase_price
        else:
            break
    elif len(value) <= 8:
        purchase_price = ord(value[0])
        if voucher_money >= purchase_price:
            others += 1
            voucher_money -= purchase_price
        else:
            break

    purchase_price = 0

print(tickets_count)
print(others)