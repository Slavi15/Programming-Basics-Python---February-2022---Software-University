N = int(input())

count = 0
array = []

for i in range(1111, 10000):
    if str(i).count('0') == 0:
        for digit in str(i):
            if N % int(digit) == 0:
                count += 1
            else:
                count = 0
                break
        if count == 4:
            count = 0
            array.append(str(i))

print(' '.join(array))