n = int(input())

value = 0
i = 1
while i <= n:
    if i == 1:
        print(1)
    else:
        print(value)

    value = (2 * i) + 1
    i = value