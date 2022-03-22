money = 0

while True:
    value = input()

    if value == "NoMoreMoney":
        break

    if float(value) < 0:
        print("Invalid operation!")
        break
    else:
        money += float(value)
        print(f"Increase: {float(value):.2f}")

print(f"Total: {money:.2f}")