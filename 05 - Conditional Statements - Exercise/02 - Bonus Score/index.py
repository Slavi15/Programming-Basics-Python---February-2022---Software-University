num = int(input())

bonus_pts = 0

if num <= 100:
    bonus_pts += 5
elif num > 100 and num <= 1000:
    bonus_pts += (num * 0.2)
elif num > 1000:
    bonus_pts += (num * 0.1)

if num % 2 == 0:
    bonus_pts += 1
elif num % 5 == 0 and num % 10 != 0:
    bonus_pts += 2

print(f"""{bonus_pts}
{num + bonus_pts}""")