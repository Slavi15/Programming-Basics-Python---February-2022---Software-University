n = int(input())
L = int(input())

array = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(97, 97 + L):
            for l in range(97, 97 + L):
                for m in range(1, n + 1):
                    if m > i and m > j:
                        chr1 = chr(k)
                        chr2 = chr(l)
                        array.append(f"{i}{j}{chr1}{chr2}{m}")

print(' '.join(array))