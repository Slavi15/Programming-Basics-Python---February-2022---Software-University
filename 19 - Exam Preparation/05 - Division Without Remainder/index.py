n = int(input())

divisible_by_two = 0
divisible_by_three = 0
divisible_by_four = 0

for i in range(0, n):
    num = int(input())

    if num % 2 == 0:
        divisible_by_two += 1
    
    if num % 3 == 0:
        divisible_by_three += 1

    if num % 4 == 0:
        divisible_by_four += 1

p1 = (divisible_by_two / n) * 100
p2 = (divisible_by_three / n) * 100
p3 = (divisible_by_four / n) * 100
print(f"""{p1:.2f}%
{p2:.2f}%
{p3:.2f}%""")