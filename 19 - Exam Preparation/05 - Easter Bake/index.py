import math

easter_bread_count = int(input())

all_sugar = 0
sugar_array = []
all_flour = 0
flour_array = []

for i in range(0, easter_bread_count):
    sugar_amount_grams = int(input())
    flour_amount_grams = int(input())

    all_sugar += sugar_amount_grams
    all_flour += flour_amount_grams

    sugar_array.append(sugar_amount_grams)
    flour_array.append(flour_amount_grams)

sugar_packets = math.ceil(all_sugar / 950)
flour_packets = math.ceil(all_flour / 750)

print(f"""Sugar: {sugar_packets}
Flour: {flour_packets}
Max used flour is {max(flour_array)} grams, max used sugar is {max(sugar_array)} grams.""")