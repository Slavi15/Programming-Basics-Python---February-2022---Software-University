men = int(input())
women = int(input())
table_count = int(input())

array = []

for j in range(1, men + 1):
    for k in range(1, women + 1):
        if len(array) == table_count:
            break
        array.append(f"({j} <-> {k})")

print(' '.join(array))