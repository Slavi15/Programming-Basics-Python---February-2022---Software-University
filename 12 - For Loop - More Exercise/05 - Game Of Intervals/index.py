moves_count = int(input())

points = 0
all_numbers = 0

from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid = 0

for i in range(moves_count):
    num = int(input())
    all_numbers += 1

    if num >= 0 and num <= 9:
        from_0_to_9 += 1
        points += (num * 0.2)
    elif num >= 10 and num <= 19:
        from_10_to_19 += 1
        points += (num * 0.3)
    elif num >= 20 and num <= 29:
        from_20_to_29 += 1
        points += (num * 0.4)
    elif num >= 30 and num <= 39:
        from_30_to_39 += 1
        points += 50
    elif num >= 40 and num <= 50:
        from_40_to_50 += 1
        points += 100
    elif num < 0 or num > 50:
        invalid += 1
        points /= 2

p1 = (from_0_to_9 / all_numbers) * 100
p2 = (from_10_to_19 / all_numbers) * 100
p3 = (from_20_to_29 / all_numbers) * 100
p4 = (from_30_to_39 / all_numbers) * 100
p5 = (from_40_to_50 / all_numbers) * 100
p6 = (invalid / all_numbers) * 100

print(f"""{points:.2f}
From 0 to 9: {p1:.2f}%
From 10 to 19: {p2:.2f}%
From 20 to 29: {p3:.2f}%
From 30 to 39: {p4:.2f}%
From 40 to 50: {p5:.2f}%
Invalid numbers: {p6:.2f}%""")