city = str(input())
sales = float(input())

commision = 0

if city == "Sofia":
    if sales >= 0 and sales <= 500:
        commision = sales * 0.05
    elif sales > 500 and sales <= 1000:
        commision = sales * 0.07
    elif sales > 1000 and sales <= 10000:
        commision = sales * 0.08
    elif sales > 10000:
        commision = sales * 0.12
    else:
        print("error")
elif city == "Varna":
    if sales >= 0 and sales <= 500:
        commision = sales * 0.045
    elif sales > 500 and sales <= 1000:
        commision = sales * 0.075
    elif sales > 1000 and sales <= 10000:
        commision = sales * 0.1
    elif sales > 10000:
        commision = sales * 0.13
    else:
        print("error")
elif city == "Plovdiv":
    if sales >= 0 and sales <= 500:
        commision = sales * 0.055
    elif sales > 500 and sales <= 1000:
        commision = sales * 0.08
    elif sales > 1000 and sales <= 10000:
        commision = sales * 0.12
    elif sales > 10000:
        commision = sales * 0.145
    else:
        print("error")
else:
    print("error")

if commision > 0:
    print(f"{commision:.2f}")