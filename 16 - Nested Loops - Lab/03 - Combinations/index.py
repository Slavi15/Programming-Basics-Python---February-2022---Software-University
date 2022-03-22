n = int(input())

combinations = 0

for i in range(0, n + 1):
    for j in range(0, n + 1):
        for k in range(0, n + 1):
            result = i + j + k
            if result == n:
                combinations += 1

print(combinations)