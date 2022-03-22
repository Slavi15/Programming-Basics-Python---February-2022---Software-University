start = int(input())
end = int(input())

array = []

for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            for l in range(start, end + 1):
                if (i % 2 == 0 and l % 2 != 0) or (i % 2 != 0 and l % 2 == 0):
                    if i > l:
                        numbers_sum = j + k
                        if numbers_sum % 2 == 0:
                            array.append(f"{i}{j}{k}{l}")

print(' '.join(array))