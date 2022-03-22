first_end = int(input())
second_end = int(input())
third_end = int(input())

array = []

for i in range(1, first_end + 1):
    for j in range(2, second_end + 1):
        for k in range(1, third_end + 1):
            if i % 2 == 0:
                if k % 2 == 0:
                    flag = 0
                    if j == 2:
                        array.append(f"{i} {j} {k}")
                        continue
                    for x in range(2, j):
                        if j % x == 0:
                            flag = 1
                            break
                    if flag == 0:
                        if k % 2 == 0:
                            array.append(f"{i} {j} {k}")

print('\n'.join(array))