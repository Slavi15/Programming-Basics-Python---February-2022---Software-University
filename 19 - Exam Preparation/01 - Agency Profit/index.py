company_name = str(input())
adult_tickets = int(input())
kid_tickets = int(input())
adult_ticket_price = float(input())
tax_service = float(input())

kid_ticket_price = (adult_ticket_price - (adult_ticket_price * 0.7)) + tax_service
adult_ticket_price += tax_service

adult_tickets_income = adult_tickets * adult_ticket_price
kid_tickets_income = kid_tickets * kid_ticket_price
all_tickets = adult_tickets_income + kid_tickets_income

final_income = all_tickets * 0.2

print(f"The profit of your agency from {company_name} tickets is {final_income:.2f} lv.")