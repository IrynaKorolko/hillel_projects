import string
new_line = input("Введіть рядок: ")
line_without_symbols = ""
for el in new_line:
    if el not in string.punctuation:
        line_without_symbols += el
line_without_space = line_without_symbols.split()
hashtag = "#" + ''.join(line_without_space)
print(hashtag[:140])