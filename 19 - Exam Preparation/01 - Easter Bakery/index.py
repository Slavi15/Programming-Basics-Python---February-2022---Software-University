flour_price_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
peels_with_eggs_count = int(input())
maya_packets = int(input())

sugar_kg_price = flour_price_kg - (flour_price_kg * 0.25)
one_peel_with_eggs_price = flour_price_kg + (flour_price_kg * 0.1)
maya_packet_price = sugar_kg_price - (sugar_kg_price * 0.8)

flour_price = flour_price_kg * flour_kg
sugar_price = sugar_kg_price * sugar_kg
peels_price = one_peel_with_eggs_price * peels_with_eggs_count
maya_price = maya_packet_price * maya_packets

expenses = flour_price + sugar_price + peels_price + maya_price
print(f"{expenses:.2f}")