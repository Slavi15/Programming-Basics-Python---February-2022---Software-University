import math

figureType = str(input())
area = 0

if figureType == "square":
    side = float(input())
    area = math.pow(side, 2)
elif figureType == "triangle":
    side1 = float(input())
    side2 = float(input())
    area = (side1 * side2) / 2
elif figureType == "rectangle":
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
elif figureType == "circle":
    r = float(input())
    pi = math.pi
    area = pi * math.pow(r, 2)

print(f"{area:.3f}")