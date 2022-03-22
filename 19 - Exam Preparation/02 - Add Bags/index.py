luggage_price_over_20kg = float(input())
luggage_kg = float(input())
days_till_travel = int(input())
luggage_count = int(input())

tax = 0

if luggage_kg < 10:
    tax = (luggage_price_over_20kg * 0.2)
elif luggage_kg >= 10 and luggage_kg <= 20:
    tax = (luggage_price_over_20kg / 2)
elif luggage_kg > 20:
    tax = luggage_price_over_20kg

if days_till_travel > 30:
    tax += (tax * 0.1)
elif days_till_travel >= 7 and days_till_travel <= 30:
    tax += (tax * 0.15)
elif days_till_travel < 7:
    tax += (tax * 0.4)

money_sum = tax * luggage_count
print(f"The total price of bags is: {money_sum:.2f} lv.")