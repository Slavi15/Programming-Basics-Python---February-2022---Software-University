M = int(input())

array = []

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if ((a * b) + (c * d)) == M:
                        array.append(f"{a}{b}{c}{d}")

if len(array) > 0:
    print(' '.join(array))
    if len(array) >= 4:
        print(f"Password: {array[3]}")
    else:
        print("No!")
else:
    print("No!")