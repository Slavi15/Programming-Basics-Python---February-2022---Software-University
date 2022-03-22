a = int(input())
b = int(input())
max_number_passwords = int(input())

i = 35
j = 64

array = []

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if len(array) == max_number_passwords:
            break

        A = chr(i)
        B = chr(j)
        array.append(f"{A}{B}{x}{y}{B}{A}|")
        
        i += 1
        j += 1
        if i == 55:
            i = 35
        if j == 96:
            j = 64

print(''.join(array))