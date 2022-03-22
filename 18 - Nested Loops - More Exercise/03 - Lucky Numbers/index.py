N = int(input())

array = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                first_sum = i + j
                second_sum = k + l
                if first_sum == second_sum:
                    if N % first_sum == 0:
                        array.append(f"{i}{j}{k}{l}")

print(' '.join(array))