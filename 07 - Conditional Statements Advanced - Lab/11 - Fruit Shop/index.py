fruit = str(input())
day_of_week = str(input())
quantity = float(input())

price = 0

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        price = quantity * 2.5
    elif fruit == "apple":
        price = quantity * 1.2
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == "grapefruit":
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity * 2.7
    elif fruit == "pineapple":
        price = quantity * 5.5
    elif fruit == "grapes":
        price = quantity * 3.85
    else:
        print("error")
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = quantity * 2.7
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.9
    elif fruit == "grapefruit":
        price = quantity * 1.6
    elif fruit == "kiwi":
        price = quantity * 3
    elif fruit == "pineapple":
        price = quantity * 5.6
    elif fruit == "grapes":
        price = quantity * 4.20
    else:
        print("error")
else:
    print("error")

if price > 0:
    print(f"{price:.2f}")