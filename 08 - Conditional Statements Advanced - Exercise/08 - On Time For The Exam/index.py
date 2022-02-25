exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_hour_to_minutes = (exam_hour * 60) + exam_minute
arrival_hour_to_minutes = (arrival_hour * 60) + arrival_minute
minutes = abs(arrival_hour_to_minutes - exam_hour_to_minutes)

if (exam_hour == arrival_hour and exam_minute > arrival_minute and minutes <= 30) or (exam_hour > arrival_hour and minutes <= 30) or (exam_hour == arrival_hour and exam_minute == arrival_minute):
    print("On time")
    if minutes > 0:
        print(f"{minutes} minutes before the start")
elif exam_hour >= arrival_hour and minutes > 30:
    print("Early")
    if minutes < 60:
        print(f"{minutes} minutes before the start")
    elif minutes >= 60:
        hours = minutes // 60
        mins = minutes % 60
        if mins < 10:
            print(f"{hours}:0{mins} hours before the start")
        else:
            print(f"{hours}:{mins} hours before the start")
elif exam_hour <= arrival_hour:
    print("Late")
    if minutes < 60:
        print(f"{minutes} minutes after the start")
    elif minutes >= 60:
        hours = minutes // 60
        mins = minutes % 60
        if mins < 10:
            print(f"{hours}:0{mins} hours after the start")
        else:
            print(f"{hours}:{mins} hours after the start")