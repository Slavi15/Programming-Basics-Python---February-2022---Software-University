a1 = int(input())
a2 = int(input())
n = int(input())

third_end = int((n / 2))

for i in range(a1, a2):
    for j in range(1, n):
        for k in range(1, third_end):
            for l in range(a1, a2):
                ascii_symbol = chr(i)
                num_sum = j + k + l
                if i % 2 != 0 and l % 2 != 0 and i == l and num_sum % 2 != 0:
                    print(f"{ascii_symbol}-{j}{k}{l}")