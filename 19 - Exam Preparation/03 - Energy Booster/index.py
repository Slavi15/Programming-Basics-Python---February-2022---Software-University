fruit_type = str(input())
set_size = str(input())
ordered_sets = int(input())

money = 0

if fruit_type == "Watermelon":
    if set_size == "small":
        money = 2 * 56
    elif set_size == "big":
        money = 5 * 28.7
elif fruit_type == "Mango":
    if set_size == "small":
        money = 2 * 36.66
    elif set_size == "big":
        money = 5 * 19.6
elif fruit_type == "Pineapple":
    if set_size == "small":
        money = 2 * 42.1
    elif set_size == "big":
        money = 5 * 24.8
elif fruit_type == "Raspberry":
    if set_size == "small":
        money = 2 * 20
    elif set_size == "big":
        money = 5 * 15.2

money *= ordered_sets

if money >= 400 and money <= 1000:
    money -= (money * 0.15)
elif money > 1000:
    money /= 2

print(f"{money:.2f} lv.")