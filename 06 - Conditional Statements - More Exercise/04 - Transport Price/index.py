kilometers = int(input())
part_of_day = str(input())

price = 0

if kilometers < 20:
    start_price = 0.7
    if part_of_day == "day":
        price = start_price + (kilometers * 0.79)
    elif part_of_day == "night":
        price = start_price + (kilometers * 0.9)
elif kilometers >= 20 and kilometers < 100:
    price = kilometers * 0.09
elif kilometers >= 100:
    price = kilometers * 0.06

print(f"{price:.2f}")