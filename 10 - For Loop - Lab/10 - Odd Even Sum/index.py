num_count = int(input())

even_sum = 0
odd_sum = 0

for i in range(num_count):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    elif i % 2 != 0:
        odd_sum += number

diff = abs(even_sum - odd_sum)
if even_sum == odd_sum:
    print(f"""Yes
    Sum = {even_sum}""")
else:
    print(f"""No
    Diff = {diff}""")