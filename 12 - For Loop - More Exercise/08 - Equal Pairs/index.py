n = int(input())

arr = []
result = 0

for i in range(n):
    num1 = int(input())
    num2 = int(input())
    result = num1 + num2

    arr.append(result)

if arr.count(result) == len(arr):
    print(f"Yes, value={result}")
else:
    min_value = min(arr)
    max_value = max(arr)
    diff = max_value - min_value
    print(f"No, maxdiff={diff}")