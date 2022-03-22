bitcoins = int(input())
chinese_wan_count = float(input())
commision = float(input())

bitcoin_money = bitcoins * 1168
wan_money_in_dollar = chinese_wan_count * 0.15
wan_in_leva = wan_money_in_dollar * 1.76

money_in_leva = bitcoin_money + wan_in_leva
money_in_euro = money_in_leva / 1.95

money = money_in_euro - (money_in_euro * (commision / 100))
print(f"{money:.2f}")