deposit_value = float(input())
deposit_deadline_months = int(input())
annual_interest_rate = float(input()) / 100

price = deposit_value + deposit_deadline_months * ((deposit_value * annual_interest_rate) / 12)
print(price)