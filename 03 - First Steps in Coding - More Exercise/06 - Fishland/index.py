salmon_price_kg = float(input())
caca_price_kg = float(input())
bonito_kg = float(input())
mackerel_kg = float(input())
shell_kg = int(input())

bonito_price_kg = salmon_price_kg + (salmon_price_kg * 0.6)
mackerel_price_kg = caca_price_kg + (caca_price_kg * 0.8)
shell_price_kg = 7.5

price = (bonito_price_kg * bonito_kg) + (mackerel_price_kg * mackerel_kg) + (shell_price_kg * shell_kg)
print(f"{price:.2f}")