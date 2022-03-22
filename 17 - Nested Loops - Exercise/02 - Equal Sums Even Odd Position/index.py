num1 = int(input())
num2 = int(input())

count = 0
even_result = 0
odd_result = 0
array = []

for i in range(num1, num2 + 1):
    for digit in str(i):
        if count % 2 == 0:
            even_result += int(digit)
        elif count % 2 != 0:
            odd_result += int(digit)
        
        count += 1
    if even_result == odd_result:
        array.append(str(i))
        even_result = 0
        odd_result = 0
    else:
        even_result = 0
        odd_result = 0

print(' '.join(array))