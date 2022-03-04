months_count = int(input())

electricity_price = 0
water_price = months_count * 20
internet_price = months_count * 15
others_price = 0

for i in range(months_count):
    electricity_receipt = float(input())
    electricity_price += electricity_receipt
    others_price += (electricity_receipt + 20 + 15) + ((electricity_receipt + 20 + 15) * 0.2)

average_price = (electricity_price + water_price + internet_price + others_price) / months_count

print(f"""Electricity: {electricity_price:.2f} lv
Water: {water_price:.2f} lv
Internet: {internet_price:.2f} lv
Other: {others_price:.2f} lv
Average: {average_price:.2f} lv""")