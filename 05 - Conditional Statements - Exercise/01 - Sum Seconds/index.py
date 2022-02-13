seconds1 = int(input())
seconds2 = int(input())
seconds3 = int(input())

seconds = seconds1 + seconds2 + seconds3

minutes = seconds // 60
seconds %= 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")