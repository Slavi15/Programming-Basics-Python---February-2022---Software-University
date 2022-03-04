num_count = int(input())
arr = []
num_sum = 0

for i in range(num_count):
    num = int(input())
    arr.append(num)

max_number = max(arr)
arr.remove(max_number)

for i in arr:
    num_sum += i

diff = abs(max_number - num_sum)
if num_sum == max_number:
    print(f"""Yes
    Sum = {max_number}""")
else:
    print(f"""No
    Diff = {diff}""")