import math

n = int(input())

for i in range(0, n + 1, 2):
    result = math.pow(2, i)
    print(math.trunc(result))