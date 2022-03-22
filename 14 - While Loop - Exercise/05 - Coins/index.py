number = float(input())

coins_count = 0

while number >= 0:
    if number == 0:
        print(coins_count)
        break

    if number >= 2:
        coins_count += 1
        number -= 2
        number = round(number, 2)
        continue

    if number >= 1:
        coins_count += 1
        number -= 1
        number = round(number, 2)
        continue

    if number >= 0.5:
        coins_count += 1
        number -= 0.5
        number = round(number, 2)
        continue

    if number >= 0.2:
        coins_count += 1
        number -= 0.2
        number = round(number, 2)
        continue

    if number >= 0.1:
        coins_count += 1
        number -= 0.1
        number = round(number, 2)
        continue

    if number >= 0.05:
        coins_count += 1
        number -= 0.05
        number = round(number, 2)
        continue

    if number >= 0.02:
        coins_count += 1
        number -= 0.02
        number = round(number, 2)
        continue

    if number >= 0.01:
        coins_count += 1
        number -= 0.01
        number = round(number, 2)
        continue