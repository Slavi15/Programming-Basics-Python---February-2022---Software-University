weights_count = int(input())

price = 0
all_tons = 0

bus_count = 0
truck_count = 0
train_count = 0

for i in range(weights_count):
    weight_tons = int(input())
    all_tons += weight_tons

    if weight_tons <= 3:
        bus_count += weight_tons
        price += (weight_tons * 200)
    elif weight_tons >= 4 and weight_tons <= 11:
        truck_count += weight_tons
        price += (weight_tons * 175)
    elif weight_tons >= 12:
        train_count += weight_tons
        price += (weight_tons * 120)

average_price = (price / all_tons)
p1 = (bus_count / all_tons) * 100
p2 = (truck_count / all_tons) * 100
p3 = (train_count / all_tons) * 100

print(f"""{average_price:.2f}
{p1:.2f}%
{p2:.2f}%
{p3:.2f}%""")