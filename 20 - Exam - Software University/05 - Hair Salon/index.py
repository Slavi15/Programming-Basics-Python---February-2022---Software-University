day_desired_income = int(input())

income = 0

while True:
    service = str(input())

    if service == "closed":
        needed_income = abs(income - day_desired_income)
        print(f"""Target not reached! You need {needed_income}lv. more.
        Earned money: {income}lv.""")
        break
    elif service == "haircut":
        haircut_type = str(input())

        if haircut_type == "mens":
            income += 15
        elif haircut_type == "ladies":
            income += 20
        elif haircut_type == "kids":
            income += 10
    elif service == "color":
        color_type = str(input())

        if color_type == "touch up":
            income += 20
        elif color_type == "full color":
            income += 30

    if income >= day_desired_income:
        print(f"""You have reached your target for the day!
        Earned money: {income}lv.""")
        break