number = int(input())

value = 0

while True:
    num = int(input())
    value += num
    
    if value >= number:
        print(value)
        break