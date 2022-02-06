annual_basketball_tax = int(input())

snickers_price = annual_basketball_tax - (annual_basketball_tax * 0.4)
equipment_price = snickers_price - (snickers_price * 0.2)
basketball_price = equipment_price / 4
accessories_price = basketball_price / 5

price = annual_basketball_tax + snickers_price + equipment_price + basketball_price + accessories_price
print(price)