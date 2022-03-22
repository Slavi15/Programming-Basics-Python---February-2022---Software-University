arr = []

while True:
    value = input()

    if value == "Stop":
        break

    arr.append(int(value))

min_number = min(arr)
print(min_number)