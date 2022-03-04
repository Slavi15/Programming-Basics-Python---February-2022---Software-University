inherited_money = float(input())
year = int(input())

age = 18
money = 0

for i in range(1800, year + 1):
    if i > 1800:
        age += 1
    
    if i % 2 == 0:
        money += 12000
    elif i % 2 != 0:
        money += (12000 + (50 * age))

diff = abs(inherited_money - money)
if inherited_money >= money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left." )
else:
    print(f"He will need {diff:.2f} dollars to survive." )