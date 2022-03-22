annual_tax = int(input())

basketball_snickers_price = annual_tax - (annual_tax * 0.4)
basketball_equipment_price = basketball_snickers_price - (basketball_snickers_price * 0.2)
basketball_price = basketball_equipment_price / 4
basketball_accessories_price = basketball_price / 5

expenses = annual_tax + basketball_snickers_price + basketball_equipment_price + basketball_price + basketball_accessories_price
print(f"{expenses:.2f}")