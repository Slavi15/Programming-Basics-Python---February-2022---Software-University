people_in_group = int(input())
nights_count = int(input())
transport_cards = int(input())
museum_tickets = int(input())

one_night_price = 20
one_card_price = 1.6
one_ticket_price = 6

nights_price = nights_count * one_night_price
transport_price = transport_cards * one_card_price
museum_price = museum_tickets * one_ticket_price

expenses_per_person = nights_price + transport_price + museum_price
all_expenses = expenses_per_person * people_in_group

all_expenses += (all_expenses * 0.25)
print(f"{all_expenses:.2f}")