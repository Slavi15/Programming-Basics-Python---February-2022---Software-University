num_count = int(input())

below_200_count = 0
between_200_399_count = 0
between_400_599_count = 0
between_600_799_count = 0
bigger_800_count = 0

for i in range(num_count):
    num = int(input())

    if num < 200:
        below_200_count += 1
    elif num >= 200 and num <= 399:
        between_200_399_count += 1
    elif num >= 400 and num <= 599:
        between_400_599_count += 1
    elif num >= 600 and num <= 799:
        between_600_799_count += 1
    elif num >= 800:
        bigger_800_count += 1

p1 = (below_200_count / num_count) * 100
p2 = (between_200_399_count / num_count) * 100
p3 = (between_400_599_count / num_count) * 100
p4 = (between_600_799_count / num_count) * 100
p5 = (bigger_800_count / num_count) * 100

print(f"""{p1:.2f}%
{p2:.2f}%
{p3:.2f}%
{p4:.2f}%
{p5:.2f}%""")