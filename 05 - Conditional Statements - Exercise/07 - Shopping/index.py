budget = float(input())
gpu_cards_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_card_price = 250
gpu_price = gpu_card_price * gpu_cards_count

cpu_price = gpu_price * 0.35
ram_price = gpu_price * 0.1

price = gpu_price + (cpu_count * cpu_price) + (ram_count * ram_price)

if gpu_cards_count > cpu_count:
    price -= (price * 0.15)

needed_money = abs(price - budget)

if budget >= price:
    print(f"You have {needed_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {needed_money:.2f} leva more!")