number_one = int(input())
number_two = int(input())
operation = str(input())

result = 0
even_odd = ""

if operation == "+":
    result = number_one + number_two
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{number_one} {operation} {number_two} = {result} - {even_odd}")
elif operation == "-":
    result = number_one - number_two
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{number_one} {operation} {number_two} = {result} - {even_odd}")
elif operation == "*":
    result = number_one * number_two
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{number_one} {operation} {number_two} = {result} - {even_odd}")
elif operation == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two
        print(f"{number_one} {operation} {number_two} = {result:.2f}")
elif operation == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two
        print(f"{number_one} {operation} {number_two} = {result}")