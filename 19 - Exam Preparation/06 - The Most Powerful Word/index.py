import math

letters_sum = 0
words_array = []
vowel_array = ['a', 'e', 'i', 'o', 'u', 'y']
most_powerful_word = ""
word_power = 0

while True:
    value = str(input())

    if value == "End of words":
        print(f"The most powerful word is {most_powerful_word} - {word_power}")
        break

    for letter in value:
        ascii_value = ord(letter)
        letters_sum += ascii_value

    if value[0].lower() in vowel_array:
        letters_sum = letters_sum * len(value)
    else:
        letters_sum = math.floor(letters_sum / len(value))

    words_array.append(letters_sum)
    if letters_sum >= max(words_array):
        most_powerful_word = value
        word_power = letters_sum

    letters_sum = 0