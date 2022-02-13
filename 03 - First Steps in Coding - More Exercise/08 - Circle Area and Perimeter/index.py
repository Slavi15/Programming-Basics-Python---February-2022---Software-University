import math

r = float(input())
pi = math.pi

area = pi * math.pow(r, 2)
circumference = 2 * pi * r

print(f"""{area:.2f}
{circumference:.2f}""")