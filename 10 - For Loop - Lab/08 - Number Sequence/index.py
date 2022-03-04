num_count = int(input())
arr = []

for i in range(num_count):
    num = int(input())
    arr.append(num)

max_number = max(arr)
min_number = min(arr)

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")