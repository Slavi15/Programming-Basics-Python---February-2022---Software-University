destination = str(input())
vacation_dates = str(input())
nights_count = int(input())

expenses = 0

if destination == "France":
    if vacation_dates == "21-23":
        expenses = nights_count * 30
    elif vacation_dates == "24-27":
        expenses = nights_count * 35
    elif vacation_dates == "28-31":
        expenses = nights_count * 40
elif destination == "Italy":
    if vacation_dates == "21-23":
        expenses = nights_count * 28
    elif vacation_dates == "24-27":
        expenses = nights_count * 32
    elif vacation_dates == "28-31":
        expenses = nights_count * 39
elif destination == "Germany":
    if vacation_dates == "21-23":
        expenses = nights_count * 32
    elif vacation_dates == "24-27":
        expenses = nights_count * 37
    elif vacation_dates == "28-31":
        expenses = nights_count * 43

print(f"Easter trip to {destination} : {expenses:.2f} leva.")