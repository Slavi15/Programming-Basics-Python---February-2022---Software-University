import math

needed_hours = int(input())
days = int(input())
workers_count_afterhours = int(input())

days_for_work = days - (days * 0.1)
work_hours = days_for_work * 8
afterhours_work = workers_count_afterhours * (2 * days)

all_hours = math.floor(afterhours_work + work_hours)
left_hours = abs(all_hours - needed_hours)

if all_hours >= needed_hours:
    print(f"Yes!{left_hours} hours left.")
elif all_hours < needed_hours:
    print(f"Not enough time!{left_hours} hours needed.")