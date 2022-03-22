n = int(input())

value = 0

for i in range(0, n):
    num = int(input())

    value += num

average = value / n
print(f"{average:.2f}")