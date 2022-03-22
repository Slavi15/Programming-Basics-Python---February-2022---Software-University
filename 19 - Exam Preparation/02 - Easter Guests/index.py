import math

guests_count = int(input())
budget_money = int(input())

one_kozunak_price = 4
one_egg_price = 0.45

needed_kozunaks = math.ceil(guests_count / 3)
needed_eggs = guests_count * 2

kozunaks_price = one_kozunak_price * needed_kozunaks
eggs_price = one_egg_price * needed_eggs
expenses = kozunaks_price + eggs_price

diff = abs(budget_money - expenses)
if budget_money >= expenses:
    print(f"""Lyubo bought {needed_kozunaks} Easter bread and {needed_eggs} eggs.
    He has {diff:.2f} lv. left.""")
else:
    print(f"""Lyubo doesn't have enough money.
    He needs {diff:.2f} lv. more.""")