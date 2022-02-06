pen_packets_count = int(input())
marker_packets_count = int(input())
cleaning_fluid_litres = int(input())
discount_percent = int(input()) / 100

pen_packet_price = 5.8
marker_packet_price = 7.2
cleaning_fluid_price = 1.2

price_without_discount = (pen_packets_count * pen_packet_price) + (marker_packets_count * marker_packet_price) + (cleaning_fluid_litres * cleaning_fluid_price)
price = price_without_discount - (price_without_discount * discount_percent)

print(price)