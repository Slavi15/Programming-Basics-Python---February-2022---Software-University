import math

x = float(input())
y = float(input())
h = float(input())

front = math.pow(x, 2) - (2 * 1.2)
back = math.pow(x, 2)
left_right = ((x * y) - (math.pow(1.5, 2))) * 2

laterals = front + back + left_right

front_back_roof = x * h
left_right_roof = (x * y) * 2

roof = front_back_roof + left_right_roof

green_litres = laterals / 3.4
red_litres = roof / 4.3

print(f"""{green_litres:.2f}
{red_litres:.2f}""")