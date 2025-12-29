import string
user_input = input("Введіть дві літери через дефіс: ")
all_letters = string.ascii_letters
letter_1 = user_input[0]
letter_2 = user_input[2]
index_1 = all_letters.index(letter_1)
index_2 = all_letters.index(letter_2)
new_line = all_letters[index_1:index_2 +1]
print(new_line)