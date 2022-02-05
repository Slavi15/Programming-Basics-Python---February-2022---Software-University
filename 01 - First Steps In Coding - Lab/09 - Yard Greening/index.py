square_meters = float(input())
one_sq_meter_price = 7.61

price = square_meters * one_sq_meter_price
discount = price * 0.18
final_price = price - discount

print(f"""The final price is: {final_price} lv.
The discount is: {discount} lv.""")