bottles_count = int(input())

detergent_mililitres = bottles_count * 750
needed_mililitres = 0
iteration_count = 0
plates_count = 0
saucepan_count = 0

while True:
    value = input()
    iteration_count += 1

    if value == "End":
        break

    if iteration_count % 3 == 0:
        needed_mililitres += int(value) * 15
        saucepan_count += int(value)
    else:
        needed_mililitres += int(value) * 5
        plates_count += int(value)

    if detergent_mililitres - needed_mililitres < 0:
        break

left_mililitres = detergent_mililitres - needed_mililitres
if left_mililitres >= 0:
    print(f"""Detergent was enough!
    {plates_count} dishes and {saucepan_count} pots were washed.
    Leftover detergent {left_mililitres} ml.""")
else:
    diff = abs(left_mililitres)
    print(f"Not enough detergent, {diff} ml. more necessary!")