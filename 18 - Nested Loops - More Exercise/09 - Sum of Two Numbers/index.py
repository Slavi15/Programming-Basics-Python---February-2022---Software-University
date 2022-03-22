start = int(input())
end = int(input())
magical_number = int(input())

count = 0
valid_sums = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        count += 1
        result = i + j

        if valid_sums == 0:
            if result == magical_number:
                valid_sums += 1
                print(f"Combination N:{count} ({i} + {j} = {magical_number})")

if valid_sums == 0:
    print(f"{count} combinations - neither equals {magical_number}")