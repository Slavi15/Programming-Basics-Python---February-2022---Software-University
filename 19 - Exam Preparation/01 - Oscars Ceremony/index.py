rent = int(input())

figurine_price = rent * 0.7
catering_price = figurine_price * 0.85
dubbing_price = catering_price / 2

money = rent + figurine_price + catering_price + dubbing_price
print(f"{money:.2f}")