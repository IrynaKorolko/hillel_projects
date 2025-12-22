import string, keyword
variable_name = input("Введіть ім'я змінної: ")
reserved_words = [
    "False", "None", "True", "and", "as", "assert", "break", "class",
    "continue", "def", "del", "elif", "else", "except", "finally",
    "for", "from", "global", "if", "import", "in", "is", "lambda",
    "nonlocal", "not", "or", "pass", "raise", "return", "try",
    "while", "with", "yield"
]
if variable_name[0].isdigit() or not variable_name.islower():
   print ("False")
for el in variable_name:
    if el in string.punctuation and el != "_":
     print("False")
if variable_name.count("_") > 1 or variable_name in reserved_words:
    print("False")
print("True")