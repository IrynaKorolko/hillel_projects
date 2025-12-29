user_input = int(input("Введіть число, цифри якого необхідно перемножити "))
while user_input > 9:
    multiply_result = 1
    str_user_input = str(user_input)
    for digit in str_user_input:
        multiply_result *= int(digit)
print(multiply_result)