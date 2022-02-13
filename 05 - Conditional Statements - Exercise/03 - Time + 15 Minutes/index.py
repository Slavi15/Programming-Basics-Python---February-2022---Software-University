hour = int(input())
minutes = int(input())

all_minutes = (hour * 60) + minutes
total_minutes = all_minutes + 15

hours = total_minutes // 60
total_minutes %= 60

if hours == 24:
    hours = 0
elif hours > 24:
    hours -= 24

if total_minutes < 10:
    print(f"{hours}:0{total_minutes}")
else:
    print(f"{hours}:{total_minutes}")