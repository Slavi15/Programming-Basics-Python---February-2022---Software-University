season = str(input())
km_per_month = float(input())

money = 0

if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        money = km_per_month * 0.75 * 4
    elif km_per_month > 5000 and km_per_month <= 10000:
        money = km_per_month * 0.95 * 4
    elif km_per_month > 10000 and km_per_month <= 20000:
        money = km_per_month * 1.45 * 4
elif season == "Summer":
    if km_per_month <= 5000:
        money = km_per_month * 0.9 * 4
    elif km_per_month > 5000 and km_per_month <= 10000:
        money = km_per_month * 1.1 * 4
    elif km_per_month > 10000 and km_per_month <= 20000:
        money = km_per_month * 1.45 * 4
elif season == "Winter":
    if km_per_month <= 5000:
        money = km_per_month * 1.05 * 4
    elif km_per_month > 5000 and km_per_month <= 10000:
        money = km_per_month * 1.25 * 4
    elif km_per_month > 10000 and km_per_month <= 20000:
        money = km_per_month * 1.45 * 4

money -= (money * 0.1)
print(f"{money:.2f}")