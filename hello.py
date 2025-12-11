# Task1
number = int(input("Введіть число:"))
number_sq = pow(number, 2)
print(number_sq)


# Task2
number1 = int(input("Введіть ціле число:"))
number2 = int(input("Введіть ціле число:"))
number_3 = int(input("Введіть ціле число:"))
average_numbers = (number1 + number2 + number_3)/3
print (average_numbers)


# Task3
minutes = int (input ("Введіть хвилини, які потрібно перетворити:"))
hours = minutes//60
minutes_left = minutes%60
print (f"{hours} години та {minutes_left}хвилин")


# Task4
price = int(input("Введіть ціну товару:"))
discount = int(input("Введіть знижку, яка буде застосовуватись:"))/100
discounted_price = price - (price * discount)
print (f"Ціна зі знижкою:{discounted_price}")


# Task5
number = input("Введіть чотиризначне число:")
last_digit = number [3]
print (last_digit)


# Task6
length_rect = float(input("Введіть довжину прямокутника:"))
width_rect = float(input("Введіть ширину прямокутника:"))
perimetr_rect = (length_rect + width_rect) * 2
print (f"Периметр прямокутника дорівнює {perimetr_rect}")


# Task7
full_number = input ("Введіть чотиризначне число:")
num_1 = full_number [0]
num_2 = full_number [1]
num_3 = full_number [2]
num_4 = full_number [3]
print (num_1)
print (num_2)
print (num_3)
print (num_4)