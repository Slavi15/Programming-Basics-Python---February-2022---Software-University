import math

people_count = int(input())
entrance_tax = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

tax_money = people_count * entrance_tax

deck_chair_people = math.ceil(people_count * 0.75)
deck_chair_money = deck_chair_people * deck_chair_price

umbrella_people = math.ceil(people_count / 2)
umbrella_money = umbrella_people * umbrella_price

final_money = tax_money + deck_chair_money + umbrella_money
print(f"{final_money:.2f} lv.")