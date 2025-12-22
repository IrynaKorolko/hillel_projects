while True:
    num1 = int(input("Введіть перше число: "))
    num2 = int(input("Введіть друге число: "))
    operation = input("Введіть операцію з числами: ")
    if operation is "+":
        print(num1 + num2)
    elif operation is "-":
        print(num1 - num2)
    elif operation is "*":
        print(num1 * num2)
    elif operation is "/":
        if num2 == 0:
            print("Ділити на нуль не можна")
        else:
            print(num1 / num2)
    next_question = input("Розпочати нове обчислення?(так/ні)")
    if next_question == "ні":
        break
