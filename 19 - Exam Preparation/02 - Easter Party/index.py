guests_count = int(input())
cover_person_price = float(input())
budget_money = float(input())

if guests_count >= 10 and guests_count <= 15:
    cover_person_price -= (cover_person_price * 0.15)
elif guests_count > 15 and guests_count <= 20:
    cover_person_price -= (cover_person_price * 0.2)
elif guests_count > 20:
    cover_person_price -= (cover_person_price * 0.25)

cake_price = budget_money * 0.1
people_price = guests_count * cover_person_price
expenses = people_price + cake_price

diff = abs(budget_money - expenses)
if budget_money >= expenses:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")