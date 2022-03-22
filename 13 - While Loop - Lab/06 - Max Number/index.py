arr = []

while True:
    value = input()

    if value == "Stop":
        break

    arr.append(int(value))

max_number = max(arr)
print(max_number)