text_array = []
array = []

excluded_count = 0
excluded_array = []

while True:
    value = input()

    if value == "End":
        break

    if value.isalpha() == True:
        if value == "c" or value == "o" or value == "n":
            if excluded_array.count(value) == 0:
                excluded_array.append(value)
                excluded_count += 1
            else:
                text_array.append(value)
        else:
            text_array.append(value)

        if excluded_count == 3:
            joined_array = ''.join(text_array)
            array.append(joined_array)
            array.append(' ')

            text_array.clear()
            excluded_array.clear()
            excluded_count = 0

print(''.join(array))