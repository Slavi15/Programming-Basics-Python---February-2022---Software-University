clients_count = int(input())

products_count = 0
expenses = 0
all_expenses = 0

for i in range(0, clients_count):
    while True:
        text = str(input())

        if text == "Finish":
            if products_count % 2 == 0:
                expenses -= (expenses * 0.2)
                all_expenses += expenses

                print(f"You purchased {products_count} items for {expenses:.2f} leva.")
                products_count = 0
                expenses = 0
            else:
                all_expenses += expenses
                print(f"You purchased {products_count} items for {expenses:.2f} leva.")
                products_count = 0
                expenses = 0
            break

        products_count += 1
        if text == "basket":
            expenses += 1.5
        elif text == "wreath":
            expenses += 3.8
        elif text == "chocolate bunny":
            expenses += 7

average_expense = all_expenses / clients_count
print(f"Average bill per client is: {average_expense:.2f} leva.")