n = int(input())

combinations_array = []

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                num_sum = a + b + c + d
                num_product = a * b * c * d

                if len(combinations_array) == 0:
                    if num_sum == num_product and n % 5 == 0 and n % 10 != 0:
                        combinations_array.append(f"{a}{b}{c}{d}")
                        break
                    elif int(num_product / num_sum) == 3 and n % 3 == 0:
                        combinations_array.append(f"{d}{c}{b}{a}")
                        break

if len(combinations_array) > 0:
    print(''.join(combinations_array))
else:
    print("Nothing found")