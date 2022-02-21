free_days = int(input())
work_days = 365 - free_days

all_minutes = (free_days * 127) + (work_days * 63)
difference = abs(30000 - all_minutes)

hours = difference // 60
minutes = difference % 60

if all_minutes > 30000:
    print(f"""Tom will run away
    {hours} hours and {minutes} minutes more for play""")
elif all_minutes <= 30000:
    print(f"""Tom sleeps well
    {hours} hours and {minutes} minutes less for play""")