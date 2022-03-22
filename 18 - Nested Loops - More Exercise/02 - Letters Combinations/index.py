start = str(input())
end = str(input())
letter = str(input())

start_number = ord(start) - 96
end_number = ord(end) - 96
letter_number = ord(letter) - 96

array = []

for i in range(start_number, end_number + 1):
    for j in range(start_number, end_number + 1):
        for k in range(start_number, end_number + 1):
            if i != letter_number:
                if j != letter_number:
                    if k != letter_number:
                        first_letter = chr(i + 96)
                        second_letter = chr(j + 96)
                        third_letter = chr(k + 96)
                        array.append(f"{first_letter}{second_letter}{third_letter}")

print(f"{' '.join(array)} {len(array)}")