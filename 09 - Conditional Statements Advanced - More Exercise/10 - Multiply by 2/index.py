while True:
    number = float(input())
    result = number * 2

    if result >= 0:
        print(f"Result: {result:.2f}")
    else:
        print("Negative number!")
        break