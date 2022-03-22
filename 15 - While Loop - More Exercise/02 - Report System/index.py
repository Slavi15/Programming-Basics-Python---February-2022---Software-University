expected_money = int(input())

iteration_count = 0
cs_money = 0
cs_count = 0
cc_money = 0
cc_count = 0

while True:
    value = input()
    iteration_count += 1

    if value == "End":
        print("Failed to collect required money for charity.")
        break

    if iteration_count % 2 == 0:
        if int(value) < 10:
            print("Error in transaction!")
        else:
            cc_money += int(value)
            cc_count += 1
            print("Product sold!")
    else:
        if int(value) > 100:
            print("Error in transaction!")
        else:
            cs_money += int(value)
            cs_count += 1
            print("Product sold!")

    all_money = 0
    all_money += (cs_money + cc_money)
    if all_money >= expected_money:
        average_cs_money = cs_money / cs_count
        average_cc_money = cc_money / cc_count

        print(f"""Average CS: {average_cs_money:.2f}
        Average CC: {average_cc_money:.2f}""")
        break