import math

prime_sum = 0
non_prime_sum = 0

while True:
    value = input()

    if value == "stop":
        break

    prime_flag = 0
    if int(value) > 1:
        for i in range(2, int(math.sqrt(int(value))) + 1):
            if (int(value) % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            prime_sum += int(value)
        else:
            non_prime_sum += int(value)
    elif int(value) < 0:
        print("Number is negative.")

print(f"""Sum of all prime numbers is: {prime_sum}
Sum of all non prime numbers is: {non_prime_sum}""")