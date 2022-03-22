import math

tennis_racquette_price = float(input())
tennis_racquette_count = int(input())
pairs_of_shoes = int(input())

pair_of_shoes_price = tennis_racquette_price / 6
all_tennis_racquettes = tennis_racquette_count * tennis_racquette_price
all_pair_of_shoes = pairs_of_shoes * pair_of_shoes_price
expenses = all_tennis_racquettes + all_pair_of_shoes

additional_equipment = expenses * 0.2

all_expenses = expenses + additional_equipment

djokovic_expenses = all_expenses / 8
sponsor_expenses = (all_expenses * 7) / 8

print(f"Price to be paid by Djokovic {math.floor(djokovic_expenses)}")
print(f"Price to be paid by sponsors {math.ceil(sponsor_expenses)}")