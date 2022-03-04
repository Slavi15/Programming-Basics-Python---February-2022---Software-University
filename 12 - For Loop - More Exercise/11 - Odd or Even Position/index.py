n = int(input())

even_arr = []
odd_arr = []

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    num = float(input())

    if i % 2 == 0:
        even_sum += num
        even_arr.append(num)
    elif i % 2 != 0:
        odd_sum += num
        odd_arr.append(num)

if len(even_arr) > 0:
    even_min = min(even_arr)
    even_max = max(even_arr)

if len(odd_arr) > 0:
    odd_min = min(odd_arr)
    odd_max = max(odd_arr)

if even_sum == 0 and odd_sum == 0:
    print(f"""OddSum={odd_sum:.2f},
    OddMin=No,
    OddMax=No,
    EvenSum={even_sum:.2f},
    EvenMin=No,
    EvenMax=No""")
elif even_sum == 0:
    print(f"""OddSum={odd_sum:.2f},
    OddMin={odd_min:.2f},
    OddMax={odd_max:.2f},
    EvenSum={even_sum:.2f},
    EvenMin=No,
    EvenMax=No""")
elif odd_sum == 0:
    print(f"""OddSum={odd_sum:.2f},
    OddMin=No,
    OddMax=No,
    EvenSum={even_sum:.2f},
    EvenMin={even_min:.2f},
    EvenMax={even_max:.2f}""")
else:
    print(f"""OddSum={odd_sum:.2f},
    OddMin={odd_min:.2f},
    OddMax={odd_max:.2f},
    EvenSum={even_sum:.2f},
    EvenMin={even_min:.2f},
    EvenMax={even_max:.2f}""")