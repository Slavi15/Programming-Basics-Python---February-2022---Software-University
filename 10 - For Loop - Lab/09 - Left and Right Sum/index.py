num = int(input())
end_num = num * 2

left_sum = 0
right_sum = 0

for i in range(num):
    left_sum += int(input())

for i in range(num, end_num):
    right_sum += int(input())

diff = abs(right_sum - left_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {diff}")